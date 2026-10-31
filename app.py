from flask import Flask

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Wireless Mouse", "price": 799},
    {"id": 2, "name": "Mechanical Keyboard", "price": 2499},
    {"id": 3, "name": "USB-C Hub", "price": 1299},
]

@app.route("/")
def home():
    return "Home"

if __name__ == "__main__":
    app.run(debug=True)