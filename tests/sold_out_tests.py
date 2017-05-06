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

    def test_when_the_item_selected_by_the_customer_is_out_of_stock_the_machine_displays_SOLD_OUT(self):
        self.VendingMachine.vending_machine_reset()
        for sale_index in range(6):
            coin = quarter
            self.VendingMachine.accept_coins(coin)
            self.VendingMachine.accept_coins(coin)
            self.VendingMachine.accept_coins(coin)
            self.VendingMachine.accept_coins(coin)
            self.VendingMachine.cola_button_press()
            print("cola_quantity->", self.VendingMachine.cola_quantity)
            print("display->", self.VendingMachine.display)

    # Once we have all the values we are changing, create this test with all values.
    # def test_vending_machine_reset_restores_initialized_values(self):
    #     coin = quarter
    #     self.VendingMachine.accept_coins(coin)

if __name__ == '__main__':
    unittest.main()
