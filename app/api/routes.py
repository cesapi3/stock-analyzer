from flask import Blueprint, jsonify, request

# Initialize blueprint
api = Blueprint('api', __name__)

# Sample Data
stocks = {
    'AAPL': {'name': 'Apple Inc.', 'price': 150, 'change': 1.2},
    'GOOGL': {'name': 'Alphabet Inc.', 'price': 2800, 'change': -15.3},
}

@api.route('/stocks', methods=['GET'])
def get_stocks():
    return jsonify(stocks)

@api.route('/stocks/<symbol>', methods=['GET'])
def get_stock(symbol):
    stock = stocks.get(symbol.upper())
    if stock:
        return jsonify(stock)
    else:
        return jsonify({'error': 'Stock not found'}), 404

@api.route('/stocks/<symbol>', methods=['POST'])
def add_stock(symbol):
    data = request.get_json()
    stocks[symbol.upper()] = data
    return jsonify({'message': 'Stock added'}), 201

@api.route('/stocks/<symbol>', methods=['PUT'])
def update_stock(symbol):
    data = request.get_json()
    if symbol.upper() in stocks:
        stocks[symbol.upper()].update(data)
        return jsonify({'message': 'Stock updated'}), 200
    else:
        return jsonify({'error': 'Stock not found'}), 404

@api.route('/stocks/<symbol>', methods=['DELETE'])
def delete_stock(symbol):
    if symbol.upper() in stocks:
        del stocks[symbol.upper()]
        return jsonify({'message': 'Stock deleted'}), 200
    else:
        return jsonify({'error': 'Stock not found'}), 404
