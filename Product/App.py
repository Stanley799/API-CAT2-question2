#this is a file for the API logic

from flask import Flask, request, jsonify

App = Flask(__name__)

# In-memory database
products = []

@App.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    
    # This validates the  input
    if not data or not all(key in data for key in ('name', 'description', 'price')):
        return jsonify({"error": "Invalid data"}), 400
    
    try:
        new_product = {
            "name": data['name'],
            "description": data['description'],
            "price": float(data['price'])
        }
        products.append(new_product)
        return jsonify(new_product), 201
    except ValueError:
        return jsonify({"error": "Invalid price"}), 400

@App.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

if __name__ == '__main__':
    App.run(debug=True)
