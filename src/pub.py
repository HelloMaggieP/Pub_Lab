class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drink = []


    def increase_till(self, drink):
        self.till += drink.price

    def check_age(self, customer):
        if customer.age >= 18:
            return True
        else:
            self.refuse_service(customer)

    def refuse_service(self, customer):
        print("Get Out")
        


        

    