from flask import Flask, jsonify, request

app = Flask(__name__)

from products import product

@app.route('/ping')
def ping():
    return jsonify({'message':'Hola manu'})

@app.route('/products')
def getproducts():
    return jsonify(product)

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productFound = [product for product in product if product['name']== product_name]
    if (len(productFound)>0):
        return jsonify({'product':productFound[0]})
    return jsonify({"message":"Product not found"})

@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    product.append(new_product)
    return jsonify({"message": "Product added succesfully","product":product})

@app.route('/products/<string:product_name>',methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in product if product['name']== product_name]
    if (len(productFound)>0):
        productFound[0]['name'] = request.json['name'],
        productFound[0]['price'] = request.json['price'],
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "Product Updated",
            "produst": productFound[0]
        })
        return jsonify({"message":"Product not found"})

@app.route('/products/<string:product_name>',methods=['DELETE'])
def deleteProduct(product_name):
    productFound = [product for product in product if product['name']== product_name]
    if (len(productFound)>0):
        product.remove(productFound[0])
        return jsonify({
            "message":"Product Delete",
            "products": product
        })
    return jsonify({"message":"Product not found"})

if __name__ == '__main__':
    app.run(debug=True, port=3010)