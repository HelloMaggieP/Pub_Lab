class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def can_afford(self, amount):
        if self.wallet >= amount:
            return True
        else:
            return False

    def reduce_wallet(self, amount):
        self.wallet -= amount
        return self.wallet

    