from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

products = []

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.get_json()
    
    if not data or 'id' not in data or 'name' not in data or 'price' not in data or 'quantity' not in data:
        return jsonify({'error': 'Faltan campos requeridos'}), 400
    
    product = {
        'id': data['id'],
        'name': data['name'],
        'price': float(data['price']),
        'quantity': int(data['quantity'])
    }
    
    products.append(product)
    return jsonify(product), 201

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [p for p in products if p['id'] != product_id]
    return jsonify({'message': 'Producto eliminado'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)