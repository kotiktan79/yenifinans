from flask import Flask, request, jsonify
import yfinance as yf
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/price", methods=["GET"])
def get_price():
    symbol = request.args.get("symbol")
    data = yf.Ticker(symbol)
    price = data.history(period="1d")['Close'].iloc[-1]
    return jsonify({"symbol": symbol, "price": float(price)})

if __name__ == "__main__":
    app.run(debug=True)