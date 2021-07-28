# tests/drink_test.py

import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink


class TestDrink(unittest.TestCase):
    
    def setUp(self): 
      self.drink = Drink("Vodka Martini", 10, 50)


    # @unittest.skip("Delete this line to run the test")
    def test_has_name(self):
        self.assertEqual("Vodka Martini", self.drink.name)

    # @unittest.skip("Delete this line to run the test")
    def test_has_price(self):
        self.assertEqual(10, self.drink.price)

    # @unittest.skip("Delete this line to run the test")
    def test_in_stock(self):
        self.assertEqual(50, self.drink.stock_level)

    # @unittest.skip("Delete this line to run the test")
    def test_reduce_stock(self):
        self.assertEqual(49, self.drink.reduce_stock())