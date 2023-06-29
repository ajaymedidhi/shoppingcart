class Cart:
    def __init__(self):
        self.items = {} 
    
    def add_items(self, item_name, quantity):
        self.items[item_name] = quantity 
    
    def remove_item(self,item_name):
        del self.items[item_name]
        
    def get_cart_items(self):
        print(self.items)
        
obj_1 = Cart()
obj_1.add_items("book",10)
obj_1.add_items("laptop",1)
obj_1.remove_item("book")
obj_1.get_cart_items()
