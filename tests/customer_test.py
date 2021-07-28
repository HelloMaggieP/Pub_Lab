# tests/customer_test.py

import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink


class TestCustomer(unittest.TestCase):
    
    def setUp(self): 
      self.customer = Customer("Bond, James Bond", 50.00)


    # @unittest.skip("Delete this line to run the test")
    def test_has_name(self):
        self.assertEqual("Bond, James Bond", self.customer.name)

    # @unittest.skip("Delete this line to run the test")
    def test_can_afford(self):
        self.assertEqual(True, self.customer.can_afford(10))

    # @unittest.skip("Delete this line to run the test")
    def test_cannot_afford(self):
        self.assertEqual(False, self.customer.can_afford(60))

     # @unittest.skip("Delete this line to run the test")
    def test_reduce_wallet(self):
        self.assertEqual(40, self.customer.reduce_wallet(10))