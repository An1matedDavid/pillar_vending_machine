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
        self.VendingMachine.vending_machine_reset()
        coin = quarter
        self.VendingMachine.accept_coins(coin)
        self.assertEqual(self.VendingMachine.current_amount, 0.25)
        self.VendingMachine.cola_button_press()
        self.assertEqual(self.VendingMachine.price, 1.00)
        self.VendingMachine._check_transaction()
        self.assertEqual(self.VendingMachine.balance, 0.75)

    def test_insert_coins_then_press_button_if_cola_transaction_amount_correct_dispense_cola(self):
        self.VendingMachine.vending_machine_reset()
        coin = quarter
        self.VendingMachine.accept_coins(coin)
        self.VendingMachine.accept_coins(coin)
        self.VendingMachine.accept_coins(coin)
        self.VendingMachine.accept_coins(coin)
        self.VendingMachine.cola_button_press()
        self.assertEqual(self.VendingMachine.dispensed_product, 'cola')

    def test_press_button_then_insert_coins_if_cola_transaction_amount_correct_dispense_cola(self):
        self.VendingMachine.vending_machine_reset()
        self.VendingMachine.cola_button_press()
        coin = quarter
        self.VendingMachine.accept_coins(coin)
        self.VendingMachine.accept_coins(coin)
        self.VendingMachine.accept_coins(coin)
        self.VendingMachine.accept_coins(coin)
        self.assertEqual(self.VendingMachine.dispensed_product, 'cola')

    def test_insert_coins_then_press_button_if_cola_transaction_amount_correct_dispense_chips(self):
        self.VendingMachine.vending_machine_reset()
        coin1 = quarter
        coin2 = quarter
        self.VendingMachine.accept_coins(coin1)
        self.VendingMachine.accept_coins(coin2)
        self.VendingMachine.chips_button_press()
        self.assertEqual(self.VendingMachine.dispensed_product, 'chips')

    def test_press_button_then_insert_coins_if_cola_transaction_amount_correct_dispense_chips(self):
        self.VendingMachine.vending_machine_reset()
        self.VendingMachine.chips_button_press()
        coin1 = quarter
        coin2 = quarter
        self.VendingMachine.accept_coins(coin1)
        self.VendingMachine.accept_coins(coin2)
        self.assertEqual(self.VendingMachine.dispensed_product, 'chips')

    def test_insert_coins_then_press_button_if_cola_transaction_amount_correct_dispense_candy(self):
        self.VendingMachine.vending_machine_reset()
        coin1 = quarter
        coin2 = quarter
        coin3 = dime
        coin4 = nickel
        self.VendingMachine.accept_coins(coin1)
        self.VendingMachine.accept_coins(coin2)
        self.VendingMachine.accept_coins(coin3)
        self.VendingMachine.accept_coins(coin4)
        self.VendingMachine.candy_button_press()
        self.assertEqual(self.VendingMachine.dispensed_product, 'candy')

    def test_press_button_then_insert_coins_if_cola_transaction_amount_correct_dispense_candy(self):
        self.VendingMachine.vending_machine_reset()
        self.VendingMachine.candy_button_press()
        coin1 = quarter
        coin2 = quarter
        coin3 = dime
        coin4 = nickel
        self.VendingMachine.accept_coins(coin1)
        self.VendingMachine.accept_coins(coin2)
        self.VendingMachine.accept_coins(coin3)
        self.VendingMachine.accept_coins(coin4)
        self.assertEqual(self.VendingMachine.dispensed_product, 'candy')

    def test_after_complete_transaction_reset_transaction(self):
        self.VendingMachine.vending_machine_reset()
        coin = quarter
        self.VendingMachine.accept_coins(coin)
        self.VendingMachine.accept_coins(coin)
        self.VendingMachine.accept_coins(coin)
        self.VendingMachine.accept_coins(coin)
        self.VendingMachine.cola_button_press()
        self.assertEqual(self.VendingMachine.selected_product, 'cola')
        self.assertEqual(self.VendingMachine.price, 1.00)
        self.assertEqual(self.VendingMachine.dispensed_product, 'cola')
        self.VendingMachine.accept_coins(coin)
        self.assertEqual(self.VendingMachine.selected_product, None)
        self.assertEqual(self.VendingMachine.price, 0)
        self.assertEqual(self.VendingMachine.dispensed_product, None)

    def test_machine_updates_display_for_current_amount_when_coins_are_accepted(self):
        self.VendingMachine.vending_machine_reset()
        coin = quarter
        self.VendingMachine.accept_coins(coin)
        self.VendingMachine.accept_coins(coin)
        self.assertEqual(self.VendingMachine.display, '0.5')

    def test_machine_displays_PRICE_if_not_enough_money_is_inserted(self):
        self.VendingMachine.vending_machine_reset()
        self.VendingMachine.candy_button_press()
        self.assertEqual(self.VendingMachine.display, 'PRICE:0.65')

    def test_make_change_correctly_reaches_zero_change_due(self):
        self.VendingMachine.vending_machine_reset()
        self.VendingMachine._make_change(-0.65)
        self.assertEqual(self.VendingMachine.change_due, 0)
        self.VendingMachine.vending_machine_reset()
        self.VendingMachine._make_change(-0.75)
        self.assertEqual(self.VendingMachine.change_due, 0)
        self.VendingMachine.vending_machine_reset()
        self.VendingMachine._make_change(-0.05)
        self.assertEqual(self.VendingMachine.change_due, 0)
        self.VendingMachine.vending_machine_reset()
        self.VendingMachine._make_change(-0.10)
        self.assertEqual(self.VendingMachine.change_due, 0)
        self.VendingMachine.vending_machine_reset()
        self.VendingMachine._make_change(-0.1005)
        self.assertEqual(self.VendingMachine.change_due, 0)

    def test_make_change_sums_correct_number_of_each_coin_in_change(self):
        self.VendingMachine.vending_machine_reset()
        self.VendingMachine._make_change(-0.65)
        # quarter, quarter, dime, nickle
        self.assertEqual(self.VendingMachine.coin_return, [{'size': 24.2, 'weight': 5.6}, {'size': 24.2, 'weight': 5.6}, {'size': 17.9, 'weight': 2.2}, {'size': 21.2, 'weight': 5}])
        self.VendingMachine.vending_machine_reset()
        self.VendingMachine._make_change(-0.75)
        # quarter, quarter, quarter
        self.assertEqual(self.VendingMachine.coin_return, [{'size': 24.2, 'weight': 5.6}, {'size': 24.2, 'weight': 5.6}, {'size': 24.2, 'weight': 5.6}])
        self.VendingMachine.vending_machine_reset()
        self.VendingMachine._make_change(-0.05)
        # nickle
        self.assertEqual(self.VendingMachine.coin_return, [{'weight': 5, 'size': 21.2}])
        self.VendingMachine.vending_machine_reset()
        self.VendingMachine._make_change(-0.10)
        # dime
        self.assertEqual(self.VendingMachine.coin_return, [{'weight': 2.2, 'size': 17.9}])
        self.VendingMachine.vending_machine_reset()
        self.VendingMachine._make_change(-25000)
        # 100,000 quarters
        self.assertEqual(len(self.VendingMachine.coin_return), 100000)

        # self.assertEqual(self.VendingMachine.change_due, 0)

    # def test_make_change_adds_correct_coins_to_coin_return(self):

    # Once we have all the values we are changing, create this test with all values.
    # def test_vending_machine_reset_restores_initialized_values(self):
    #     coin = quarter
    #     self.VendingMachine.accept_coins(coin)

if __name__ == '__main__':
    unittest.main()
