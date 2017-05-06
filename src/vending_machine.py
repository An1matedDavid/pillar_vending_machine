__author__ = 'MrJ'
import math
quarter = {'weight': 5.6, 'size': 24.2}
dime = {'weight': 2.2, 'size': 17.9}
nickel = {'weight': 5, 'size': 21.2}
penny = {'weight': 2.5, 'size': 19}


class VendingMachine:

    current_amount = 0
    coin_return = []
    change_due = 0
    display = "INSERT COIN"
    price = 0
    balance = 0
    selected_product = None
    dispensed_product = None
    cola_quantity = 5
    chips_quantity = 5
    candy_quantity = 5
    quarter_quantity = 8
    dime_quantity = 8
    nickel_quantity = 8

    def vending_machine_reset(self):
        self.current_amount = 0
        self.coin_return = []
        self.display = "INSERT COIN"
        self.price = 0
        self.balance = 0
        self.selected_product = None
        self.dispensed_product = None
        self.cola_quantity = 5
        self.chips_quantity = 5
        self.candy_quantity = 5
        self.quarter_quantity = 8
        self.dime_quantity = 8
        self.nickel_quantity = 8

    def new_transaction(self):
        self.current_amount = 0
        self.coin_return = []
        self.display = "INSERT COIN"
        self.price = 0
        self.balance = 0
        self.selected_product = None
        self.dispensed_product = None

    def accept_coins(self, coin):
        is_valid = self.is_valid_coin(coin)
        if is_valid is True:
            self.add_coin_value_to_current_amount(coin)
        else:
            self.coin_return.append(coin)
        return coin

    def is_valid_coin(self, coin):
        valid_coin = False
        # quarter
        if coin['weight'] == 5.6 and coin['size'] == 24.2:
            valid_coin = True
        # dime
        elif coin['weight'] == 2.2 and coin['size'] == 17.9:
            valid_coin = True
        # nickel
        elif coin['weight'] == 5 and coin['size'] == 21.2:
            valid_coin = True
        return valid_coin

    def add_coin_value_to_current_amount(self, coin):
        # quarter
        if coin['weight'] == 5.6 and coin['size'] == 24.2:
            self._check_for_new_transaction()
            self.current_amount += 0.25
            self._coin_display()
            self._check_transaction()
        # dime
        elif coin['weight'] == 2.2 and coin['size'] == 17.9:
            self._check_for_new_transaction()
            self.current_amount += 0.10
            self._coin_display()
            self._check_transaction()
        # nickel
        elif coin['weight'] == 5 and coin['size'] == 21.2:
            self._check_for_new_transaction()
            self.current_amount += 0.05
            self._coin_display()
            self._check_transaction()

    def _coin_display(self):
        # display current amount
        current_amount = str(self.current_amount)
        self.display = current_amount

    def cola_button_press(self):
        if self.cola_quantity > 0:
            self._check_for_new_transaction()
            self.price = 1.00
            self.selected_product = "cola"
            self._button_display()
            self._check_transaction()
        else:
            self.display = "SOLD OUT"

    def chips_button_press(self):
        if self.chips_quantity > 0:
            self._check_for_new_transaction()
            self.price = 0.50
            self.selected_product = "chips"
            self._button_display()
            self._check_transaction()
        else:
            self.display = "SOLD OUT"

    def candy_button_press(self):
        if self.candy_quantity > 0:
            self._check_for_new_transaction()
            self.price = 0.65
            self.selected_product = "candy"
            self._button_display()
            self._check_transaction()
        else:
            self.display = "SOLD OUT"

    def _button_display(self):
        if self.price != 0:
            self.balance = self.price - self.current_amount
            # display price
            if self.balance > 0:
                price = "PRICE:"
                price += str(self.price)
                self.display = price

    def _check_transaction(self):
        if self.price != 0:
            self.balance = self.price - self.current_amount
            # if balance == 0, dispense and end transaction.
            if self.balance == 0:
                self._dispense_product()
            # if balance < 0, do "make change" things.
            if self.balance < 0:
                self._dispense_product()
                self._make_change(self.balance)

    def _check_for_new_transaction(self):
        if self.display == "THANK YOU":
            self.new_transaction()

    def _dispense_product(self):
        self.dispensed_product = self.selected_product
        self.display = "THANK YOU"
        if self.selected_product == "cola":
            self.cola_quantity -= 1
        elif self.selected_product == "chips":
            self.chips_quantity -= 1
        elif self.selected_product == "candy":
            self.candy_quantity -= 1

    def _make_change(self, balance):
        quarters = 0
        dimes = 0
        nickels = 0
        self.change_due = abs(balance)
        # change_due = round(change_due, 2)
        # quarters
        while self.change_due > 0:
            self.change_due -= 0.25
            # change_due = round(change_due, 2)
            quarters += 1
        if round(self.change_due, 2) < 0:
            self.change_due += 0.25
            # change_due = round(change_due, 2)
            quarters -= 1
        # dimes
        while self.change_due > 0:
            self.change_due -= 0.10
            # change_due = round(change_due, 2)
            dimes += 1
        if round(self.change_due, 2) < 0:
            self.change_due += 0.10
            # change_due = round(change_due, 2)
            dimes -= 1
        # nickels
        while self.change_due > 0:
            self.change_due -= 0.05
            # change_due = round(change_due, 2)
            nickels += 1
        if round(self.change_due, 2) < 0:
            self.change_due += 0.05
            self.change_due = round(self.change_due, 2)
            nickels -= 1
        self.change_due = round(self.change_due, 2)

        for quarter_index in range(quarters):
            self.coin_return.append(quarter)

        for dime_index in range(dimes):
            self.coin_return.append(dime)

        for nickel_index in range(nickels):
            self.coin_return.append(nickel)
