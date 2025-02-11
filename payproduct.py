class officialcallprices:
    def __init__(self):
        self.data = {}
        self.cash = 0
    
    
    def set_product_price(self, product, price):
        self.data[product] = price
        
        
    def get_price(self, product):
        return self.data.get(product)
    
    def get_productprice(self, price):
        return [product for product, p in self.data.items() if p == price]

    
        
    def pay(self, cash, product):
        
        price = self.get_price(product)
        
        if price is None:
            return "product is None please check produce name"
        
        self.cash += cash # 50000
        
        if self.cash >= price: #50000 > 60000
            change = self.cash - price
            self.cash = 0
            return f"Thank you for your purchase. Change"
        else:
            return f"Not enough cash"
    


store = officialcallprices()
store.set_product_price("Iphone 15", 30000)
store.set_product_price("MacBook Pro", 60000)
store.set_product_price("iPad Air", 20000)

product =  "MacBook Pro"
cash = 60000

result = store.pay(cash, product)
print(result) 

