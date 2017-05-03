__author__ = 'David Carroll'
import unittest
from src.vending_machine import VendingMachine

# size = mm diameter
# weight = g
quarter = {'weight': 5.6, 'size': 24.2}
dime = {'weight': 2.2, 'size': 17.9}
nickel = {'weight': 5, 'size': 21.2}
penny = {'weight': 2.5, 'size': 19}

class TestAcceptCoins(unittest.TestCase):
    # def __int__(self):
    #     self.VendingMachine = VendingMachine()

    def test_when_vending_machine_is_passed_a_coin_value_it_returns_that_value(self):
        self.VendingMachine = VendingMachine()
        coin = 5
        self.assertEqual(self.VendingMachine.accept_coins(coin), 5)

    def test_when_vending_machine_is_passed_a_coin_it_returns_that_coin(self):
        self.VendingMachine = VendingMachine()
        coin = quarter
        self.assertEqual(self.VendingMachine.accept_coins(coin), quarter)

# AcceptCoins = TestAcceptCoins()
# AcceptCoins.test_when_vending_machine_is_passed_a_coin_it_evaluates_that_coin()

if __name__ == '__main__':
    unittest.main()
