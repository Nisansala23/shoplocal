from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "T-Shirt",    "price": 10, "desc": "Classic cotton tee"},
    {"id": 2, "name": "Sneakers",   "price": 50, "desc": "Everyday comfort shoes"},
    {"id": 3, "name": "Cap",        "price": 15, "desc": "Adjustable baseball cap"},
    {"id": 4, "name": "Backpack",   "price": 40, "desc": "Lightweight 20L pack"},
    {"id": 5, "name": "Sunglasses", "price": 25, "desc": "UV400 protection lenses"},
    {"id": 6, "name": "Watch",      "price": 80, "desc": "Minimalist quartz watch"},
]

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/products")
def get_products():
    return jsonify(products)

@app.route("/products/<int:product_id>")
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
