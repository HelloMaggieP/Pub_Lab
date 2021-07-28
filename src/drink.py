class Drink:
    def __init__(self, name, price, stock_level):
        self.name = name
        self.price = price
        self.stock_level = stock_level

        
    def reduce_stock(self):
        self.stock_level -= 1
        return self.stock_level