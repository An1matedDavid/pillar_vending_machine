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

    VendingMachine = VendingMachine()

    def test_when_vending_machine_is_passed_a_coin_it_returns_that_coin(self):
        coin = quarter
        self.assertEqual(self.VendingMachine.accept_coins(coin), quarter)
        self.VendingMachine.vending_machine_reset()

    def test_when_vending_machine_is_passed_a_valid_coin_it_updates_current_amount(self):
        coin1 = quarter
        self.VendingMachine.accept_coins(coin1)
        self.assertEqual(self.VendingMachine.current_amount, 0.25)
        self.assertEqual(self.VendingMachine.coin_return, [])
        coin3 = dime
        self.VendingMachine.accept_coins(coin3)
        self.assertEqual(self.VendingMachine.current_amount, 0.35)
        self.assertEqual(self.VendingMachine.coin_return, [])

    def test_when_vending_machine_is_passed_an_invalid_coin_it_is_added_to_return(self):
        coin2 = penny
        self.VendingMachine.accept_coins(coin2)
        self.assertEqual(self.VendingMachine.current_amount, 0.35)
        self.assertEqual(self.VendingMachine.coin_return, [{'size': 19, 'weight': 2.5}])

    def test_when_product_is_selected_price_is_set(self):
        self.VendingMachine.cola_button_press()
        self.assertEqual(self.VendingMachine.price, 1.00)
        self.VendingMachine.chips_button_press()
        self.assertEqual(self.VendingMachine.price, 0.50)
        self.VendingMachine.candy_button_press()
        self.assertEqual(self.VendingMachine.price, 0.65)

    def test_check_transaction_for_correct_balance(self):
        coin = quarter
        self.VendingMachine.accept_coins(coin)
        self.VendingMachine.cola_button_press()
        self.VendingMachine._check_transaction()
        self.assertEqual(self.VendingMachine.balance, 0.75)

if __name__ == '__main__':
    unittest.main()
