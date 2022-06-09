from cmath import log
from pymongo import MongoClient
from bson import ObjectId

class PurchasesDBDal:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["Project"]
        
    @property
    def purchases_db(self):
        return self.__db["Purchases"]


    def get_all_purchases(self):
        purchases = []
        cus = self.purchases_db.find({})
        for purchase in cus:
            purchases.append(purchase)
        return purchases
    
    def get_purchase_by_id(self,id):
        purchase_by_id=self.purchases_db.find_one({'_id': ObjectId(id)})
        return purchase_by_id
    
    def add_purchase(self, obj):
        
        
        self.purchases_db.insert_one(obj)
        
        
        
        
    def update_purchase(self, id, obj):
     self.purchases_db.update_one({'_id': ObjectId(id)}, {"$set": obj})

    def delete_purchase(self, id):
        self.purchases_db.delete_one({'_id': ObjectId(id)})
        return "Deleted!"
    
    def delete_related_purchases_for_product(self,pid):
        self.purchases_db.delete_many({"ProcutsId":pid})
        
    def delete_related_purchases_for_customer(self,cid):
        self.purchases_db.delete_many({"CustomerID":cid})
    
    def get_purchases_for_customer(self, cid):
        purchases = []
        # print(cid)
        cus = self.purchases_db.find({'CustomerID':cid})
        for purchase in cus:
            purchases.append(purchase)
        return purchases
 
    def get_purchases_for_product(self, pid):
        purchases=[]
        cus = self.purchases_db.find({'ProductID':pid})
        for purchase in cus:
            purchases.append(purchase)
        return purchases
    
    def search2(self,cid,pid,date):
        purchases=[]
        query = {}
      
        if cid:
            query['CustomerID'] = cid
        if pid:
            query['ProductID'] = pid
        if date:
            query['Date'] = date
        
        cus = self.purchases_db.find(query)
        
        for pur in cus:
            purchases.append(pur)

         
        return purchases



                
                

         

        
    
    def get_purchase_counter(self):
        purchases = []
        cus = self.purchases_db.find({})
        for purchase in cus:
            purchases.append(purchase)
        return len(purchases)
        