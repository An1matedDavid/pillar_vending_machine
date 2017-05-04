__author__ = 'MrJ'


class VendingMachine:

    current_amount = 0
    coin_return = []
    display = "INSERT COIN"
    price = 0
    balance = 0
    selected_product = None
    dispensed_product = None
    cola_quantity = 5

    def vending_machine_reset(self):
        self.current_amount = 0
        self.coin_return = []
        self.display = "INSERT COIN"
        self.price = 0
        self.balance = 0
        self.selected_product = None
        self.dispensed_product = None
        self.cola_quantity = 5

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
            self.current_amount += 0.25
            self._check_transaction()
        # dime
        elif coin['weight'] == 2.2 and coin['size'] == 17.9:
            self.current_amount += 0.10
            self._check_transaction()
        # nickel
        elif coin['weight'] == 5 and coin['size'] == 21.2:
            self.current_amount += 0.05
            self._check_transaction()

    def cola_button_press(self):
        self.price = 1.00
        self.selected_product = "cola"
        self._check_transaction()

    def chips_button_press(self):
        self.price = 0.50
        self.selected_product = "chips"
        self._check_transaction()

    def candy_button_press(self):
        self.price = 0.65
        self.selected_product = "candy"
        self._check_transaction()

    def _check_transaction(self):
        if self.price != 0:
            self.balance = self.price - self.current_amount
            # if balance > 0, do "need more money" things

            # if balance == 0, dispense and end transaction.
            if self.balance == 0:
                self._dispense_product()

            # if balance < 0, do "make change" things.

    def _dispense_product(self):
        self.dispensed_product = self.selected_product
