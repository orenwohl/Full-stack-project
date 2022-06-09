from flask import Flask, jsonify,request
from bson import ObjectId
import json
from datetime import *


from flask_cors import CORS

from BL.CostumersBL import *
from BL.ProductsBL import * 
from BL.PurchasesBL import * 

app = Flask(__name__)

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(MyEncoder, self).default(obj)
    
app.json_encoder = MyEncoder


CORS(app)

customers_bl = CustomersBl()
products_bl=ProductsBl()
purchases_bl=PurchasesBl()



# Customers routes

@app.route('/customers', methods=['GET'])
def get_all_customers():
    return jsonify(customers_bl.get_all_customers())

@app.route('/customers/<string:id>', methods=['GET'])
def get_customer_by_id(id):
    customer_by_id = customers_bl.get_customer_by_id(id)
    return jsonify(customer_by_id)

@app.route('/customers', methods=['POST'])
def add_customer():
    status = customers_bl.add_customer(request.json)
    return jsonify(status)


@app.route('/customers/<string:id>', methods=['PUT'])
def update_customer(id):
    status = customers_bl.update_customer(id,request.json)
    return jsonify(status)


@app.route('/customers/<string:id>', methods=['DELETE'])
def delete_person(id):
    status = customers_bl.delete_customer(id)
    return jsonify(status)

# Products routes

@app.route('/products', methods=['GET'])
def get_all_products():
    return jsonify(products_bl.get_all_products())

@app.route('/products/<string:id>', methods=['GET'])
def get_prodduct_by_id(id):
    product_by_id = products_bl.get_product_by_id(id)
    return jsonify(product_by_id)

@app.route('/products', methods=['POST'])
def add_product():
    status = products_bl.add_product(request.json)
    return jsonify(status)

@app.route('/products/<string:id>', methods=['PUT'])
def update_product(id):
    status = products_bl.update_product(id,request.json)
    return jsonify(status)

@app.route('/products/<string:id>', methods=['DELETE'])
def delete_product(id):
    status = products_bl.delete_product(id)
    return jsonify(status)

# Purchases routes

@app.route('/purchases', methods=['GET'])
def get_all_purchases():

    return jsonify(purchases_bl.get_all_purchases())

@app.route('/purchases/<string:id>', methods=['GET'])
def get_purchase_by_id(id):
    purchase_by_id = purchases_bl.get_pruchase_by_id(id)
    return jsonify(purchase_by_id)

@app.route('/purchases', methods=['POST'])
def add_purchase():
    date=datetime.now()


    status = purchases_bl.add_purchase(request.json,str(date))
    return jsonify(status)

@app.route('/purchases/<string:id>', methods=['PUT'])
def update_purchase(id):
    status = purchases_bl.update_purchase(id,request.json)
    return jsonify(status)

@app.route('/purchases/<string:id>', methods=['DELETE'])
def delete_purchase(id):
    status = purchases_bl.delete_purchase(id)
    return jsonify(status)

@app.route('/purchases/search/',methods=["get"])
def get_purchase_by_customer():
    args=request.args
    cid=args.get("cid")
    pid=args.get("pid")
    date=args.get("date")

    status=purchases_bl.search(cid,pid,date)
    return jsonify(status)

@app.route('/purchases/sea/',methods=["get"])
def get_purchase_by_customer2():
    args=request.args
    cid=args.get("cid")
    pid=args.get("pid")
    date=args.get("date")

    status=purchases_bl.search(cid,pid,date)
    return jsonify(status)

@app.route('/purchases/search/pro/<string:pid>',methods=["get"])
def get_purchase_by_product(pid):
    status=purchases_bl.get_purchases_for_produt(pid)
    return jsonify(status)

@app.route('/purchases/counter')
def purchase_counter():
    status=purchases_bl.purchases_counter()
    return jsonify(status)


app.run()
