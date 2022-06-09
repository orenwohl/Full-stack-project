from DAL.CostumersDAL import *
from DAL.PurchasesDAL import *
from bson import ObjectId


class CustomersBl:
    def __init__(self):
        self.__customers_db = CustomersDBDal()
        self.__purchases_db=PurchasesDBDal()
      
        
    def get_all_customers(self):

        return self.__customers_db.get_all_customers()
    
    def get_customer_by_id(self, id):
        customer_by_id=self.__customers_db.get_customer_by_id(id)
        return customer_by_id
    
    def add_customer(self, new_customer):
        
        new_customer={
  
    "First Name" : new_customer["First Name"],
    "Last Name" : new_customer["Last Name"],
    "City" : new_customer["City"]
        }
      
        self.__customers_db.add_customer(new_customer)

     

        return new_customer
    
    def update_customer(self,id,obj):
      new = {}
      new["First Name"] = obj["First Name"]
      new["Last Name"] = obj["Last Name"]
      new["City"] = obj["City"]
      
      self.__customers_db.update_customer(id,obj)
      
      return new
  
  
    def delete_customer(self,id):
        self.delete_related_purchases_for_customer(id)
        self.__customers_db.delete_customer(id)
        
        return "deleted"
    
    def delete_related_purchases_for_customer(self, cid):
        self.__purchases_db.delete_related_purchases_for_customer(cid)
       
       
        
        # customers.find({'_id': ObjectId(id)})
        # return a
       
       
        # for customer in customers:
        #     if ObjectId(id)  == customer["_id"]:
        #         return customer

    


 