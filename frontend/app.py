import os
import requests
from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "shoplocal-secret-key"

PRODUCTS_URL = os.getenv("PRODUCTS_SERVICE_URL", "http://localhost:5001")

def get_products():
    try:
        response = requests.get(f"{PRODUCTS_URL}/products", timeout=5)
        response.raise_for_status()
        return response.json(), None
    except Exception as e:
        return [], str(e)

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/")
def index():
    products, error = get_products()
    return render_template("index.html", products=products[:3], error=error)

@app.route("/products")
def products():
    items, error = get_products()
    cart = session.get("cart", [])
    return render_template("products.html", products=items, error=error, cart_count=len(cart))

@app.route("/cart/add/<int:product_id>")
def add_to_cart(product_id):
    products, _ = get_products()
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        cart = session.get("cart", [])
        cart.append(product)
        session["cart"] = cart
    return redirect(url_for("products"))

@app.route("/cart/remove/<int:index>")
def remove_from_cart(index):
    cart = session.get("cart", [])
    if 0 <= index < len(cart):
        cart.pop(index)
        session["cart"] = cart
    return redirect(url_for("cart"))

@app.route("/cart")
def cart():
    cart = session.get("cart", [])
    total = sum(item["price"] for item in cart)
    return render_template("cart.html", cart=cart, total=total)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
