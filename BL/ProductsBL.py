from DAL.ProductsDAL import *
from DAL.PurchasesDAL import *


class ProductsBl:
    def __init__(self):
     self.__products_db=ProductsDBDal()
     self.__purchases_db=PurchasesDBDal()
     

    def get_all_products(self):
        return self.__products_db.get_all_products()

    def get_product_by_id(self, id):
        product_by_id=self.__products_db.get_prodcut_by_id(id)
        return product_by_id
    
    def add_product(self, new_product):
        
        new_product={
  
    "Name" : new_product["Name"],
    "Price" : new_product["Price"],
    "Quantity" : new_product["Quantity"]
        }
      
        self.__products_db.add_product(new_product)

     

        return new_product
    
    def update_product(self,id,obj):
      new = {}
      new["Name"] = obj["Name"]
      new["Price"] = obj["Price"]
      new["Quantity"] = obj["Quantity"]
      
      self.__products_db.update_product(id,obj)
      
      return new
  
    def delete_product(self,id):
        self.delete_related_purchases_for_product(id)
        self.__products_db.delete_product(id)
        
        return "deleted"
    

    
    def delete_related_purchases_for_product(self, product_id):
        self.__purchases_db.delete_related_purchases_for_product(product_id)
        
        return "deleted"
    
    def get_all_customers_for_product(self):
        pass
 