class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.drink = 0
        self.age = age

    def can_afford(self, drink):
        if self.wallet >= drink.price:
            return True
        else:
            print("You don't have enough money, Mr Bond!")
            return False

    def reduce_wallet(self, drink):
        self.wallet -= drink.price
        return self.wallet

    def buy_drink(self, pub, drink):
        if pub.check_age():
            if self.can_afford(drink):
                self.reduce_wallet(drink)
                pub.increase_till(drink)
                drink.reduce_stock()
                self.drink += 1
        return self.drink


    