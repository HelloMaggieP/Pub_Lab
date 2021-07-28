class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drink = []


    def increase_till(self, drink):
        self.till += drink.price
        

    