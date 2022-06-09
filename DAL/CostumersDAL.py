from pymongo import MongoClient
from bson import ObjectId


class CustomersDBDal:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["Project"]
        
    @property
    def customers_db(self): 
        return self.__db["Customers"]

    def get_all_customers(self):
        customers = []
        cus = self.customers_db.find({})
        for customer in cus:
            customers.append(customer)
        return customers
    
    def get_customer_by_id(self,id):
        customer_by_id=self.customers_db.find_one({'_id': ObjectId(id)})
        return customer_by_id
    
    def add_customer(self, obj):
        self.customers_db.insert_one(obj)
        
        
        
    def update_customer(self, id, obj):
     

        self.customers_db.update_one({'_id': ObjectId(id)}, {"$set": obj})

    def delete_customer(self, id):
        self.customers_db.delete_one({'_id': ObjectId(id)})
        return "Deleted!"
        
        

 
  