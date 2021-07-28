class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.drink = 0

    def can_afford(self, drink):
        if self.wallet >= drink.price:
            return True
        else:
            print("You don't have enough money, Mr Bond!")
            return False

    def reduce_wallet(self, drink):
        self.wallet -= drink.price
        return self.wallet

    # def buy_drink(self, pub, drink):
        
    #     cost = drink.price
    #     if self.can_afford(cost):
    #         self.reduce_wallet(cost)
    #         pub.increase_till(drink)
    #         drink.reduce_stock()
    #         self.drink += 1
    #     return self.drink


    