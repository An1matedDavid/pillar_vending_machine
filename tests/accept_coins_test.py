__author__ = 'David Carroll'
import unittest
from src.vending_machine import VendingMachine


class TestAcceptCoins(unittest.TestCase):
    # def __int__(self):
    #     self.VendingMachine = VendingMachine()

    def test_when_vending_machine_is_passed_a_coin_it_returns_that_coin(self):
        self.VendingMachine = VendingMachine()
        coin = 5
        self.assertEqual(self.VendingMachine.accept_coins(coin), 5)

# AcceptCoins = TestAcceptCoins()
# AcceptCoins.test_when_vending_machine_is_passed_a_coin_it_evaluates_that_coin()

if __name__ == '__main__':
    unittest.main()
