from http.client import OK
from DAL.PurchasesDAL import *
from DAL.CostumersDAL import *
from DAL.ProductsDAL import *


class PurchasesBl:
    def __init__(self):
      self.__purchases_db=PurchasesDBDal()
      self.__products_db=ProductsDBDal()
    #   self__customers_db=CustomersDBDal()
    #   cid=self__customers_db["id"]

    def get_all_purchases(self):
        return self.__purchases_db.get_all_purchases()

    def get_pruchase_by_id(self, id):
        purchase_by_id=self.__purchases_db.get_purchase_by_id(id)
        return purchase_by_id

    def add_purchase(self, new_purchase,date):
        
        new_purchase={
  
    "CustomerID" : new_purchase["CustomerID"],
    "ProductID" : new_purchase["ProductID"],
    "Date" : date
        }
        check=self.__products_db.decrease_one(new_purchase["ProductID"])
        if check ==True:
         self.__purchases_db.add_purchase(new_purchase)
         return new_purchase
        else: raise Exception

     

    
    # def update_purchase(self,id,obj):
    #   new = {}
    #   new["Name"] = obj["Name"]
    #   new["Price"] = obj["Price"]
    #   new["Quantity"] = obj["Quantity"]
      
    #   self.__products_db.update_product(id,obj)
      
    #   return new
    
    def decrease_one(self,pid):
        self.__products_db.decrease_one(pid)
        return "decreases"
  
    def delete_purchase(self,id):
        self.__purchases_db.delete_purchase(id)
        
        return "deleted"
    
    def get_purchases_for_customer(self, cid):
        return self.__purchases_db.get_purchases_for_customer(cid)
    
    def search(self,cid,pid,date):
        return self.__purchases_db.search2(cid,pid,date)
    

    
    def get_purchases_for_produt(self, pid):
        return self.__purchases_db.get_purchases_for_product(pid)
    
    def purchases_counter(self):
        return self.__purchases_db.get_purchase_counter()
 