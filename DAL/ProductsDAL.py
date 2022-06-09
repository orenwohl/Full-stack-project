from http.client import OK
from pymongo import MongoClient
from bson import ObjectId

class ProductsDBDal:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["Project"]

    @property
    def products_db(self):
        return self.__db["Products"]
    
    def get_all_products(self):
        products = []
        cus = self.products_db.find({})
        for product in cus:
            products.append(product)
        return products
    
    def get_prodcut_by_id(self,id):
        product_by_id=self.products_db.find_one({'_id': ObjectId(id)})
        return product_by_id
    
    def add_product(self, obj):
        self.products_db.insert_one(obj)
    
    def decrease_one(self,pid):
        product_by_id=self.products_db.find_one({'_id': ObjectId(pid)})
        if product_by_id["Quantity"]>0:
         product_by_id["Quantity"]=product_by_id["Quantity"]-1
         new=product_by_id["Quantity"]
         self.products_db.update_one({'_id': ObjectId(pid)}, {"$set": {"Quantity":new}})
         return True
        else:return
        
        
        
        
        
        
        
    def update_product(self, id, obj):
     self.products_db.update_one({'_id': ObjectId(id)}, {"$set": obj})

    def delete_product(self, id):
        
        self.products_db.delete_one({'_id': ObjectId(id)})
        return "Deleted!"

 