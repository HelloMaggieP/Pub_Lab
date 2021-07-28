class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.drink = 0

    def can_afford(self, amount):
        if self.wallet >= amount:
            return True
        else:
            return False

    def reduce_wallet(self, amount):
        self.wallet -= amount
        return self.wallet

    def buy_drink(self, pub, drink):
        
        cost = drink.price
        if self.can_afford(cost):
            self.reduce_wallet(cost)
            pub.increase_till(drink)
            drink.reduce_stock()
            self.drink += 1
        return self.drink


    