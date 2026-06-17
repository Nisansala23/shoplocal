import os
import requests
from flask import Flask, render_template

app = Flask(__name__)

PRODUCTS_URL = os.getenv("PRODUCTS_SERVICE_URL", "http://localhost:5001")

@app.route("/health")
def health():
    return {"status": "ok"}

@app.route("/")
def index():
    try:
        response = requests.get(f"{PRODUCTS_URL}/products", timeout=5)
        response.raise_for_status()
        products = response.json()
        return render_template("index.html", products=products, error=None)
    except Exception as e:
        return render_template("index.html", products=[], error=str(e))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
