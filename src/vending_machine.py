__author__ = 'MrJ'
import math
quarter = {'weight': 5.6, 'size': 24.2}
dime = {'weight': 2.2, 'size': 17.9}
nickel = {'weight': 5, 'size': 21.2}
penny = {'weight': 2.5, 'size': 19}


class VendingMachine:

    current_amount = 0
    coin_return = []
    coins_customer_has_inserted_during_this_transaction = []
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
    # used in test suite to indicate that we only want printouts and breakpoints on data
    # from the specified test.
    print_and_break_on_this_test = False

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
        self.print_and_break_on_this_test = False
        self.coins_customer_has_inserted_during_this_transaction = []

    def new_transaction(self):
        self.current_amount = 0
        self.coin_return = []
        need_exact_change= self.check_change_making_ability()
        if need_exact_change == False:
            self.display = "INSERT COIN"
        self.price = 0
        self.balance = 0
        self.selected_product = None
        self.dispensed_product = None
        self.coins_customer_has_inserted_during_this_transaction = []

    def check_change_making_ability(self):
        """
        The most change that can be required is 0.20
        However, because the machine can always return any coin above the price of the item,
        the total change needed will only ever be .10, or .05, plus the excess coins the user entered.
        For this reason all change can be handled with either a single nickle or a single time.
        Per the recs doc, we are setting the display to "EXACT CHANGE ONLY" if any of those 2
        conditions cannot be met.
        """
        need_exact_change = False
        # cannot make change for any purchase
        if self.dime_quantity < 1 or self.nickel_quantity < 1:
            self.display = "EXACT CHANGE ONLY"
            need_exact_change = True
        return need_exact_change

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
            self.quarter_quantity += 1
            self.coins_customer_has_inserted_during_this_transaction.append(quarter)
            self._coin_display()
            self._check_transaction()
        # dime
        elif coin['weight'] == 2.2 and coin['size'] == 17.9:
            self._check_for_new_transaction()
            self.current_amount += 0.10
            self.dime_quantity += 1
            self.coins_customer_has_inserted_during_this_transaction.append(dime)
            self._coin_display()
            self._check_transaction()
        # nickel
        elif coin['weight'] == 5 and coin['size'] == 21.2:
            self._check_for_new_transaction()
            self.current_amount += 0.05
            self.nickel_quantity += 1
            self.coins_customer_has_inserted_during_this_transaction.append(nickel)
            self._coin_display()
            self._check_transaction()

    def _coin_display(self):
        self.check_change_making_ability()
        # display current amount
        current_amount = str(self.current_amount)
        self.display = current_amount

    def cola_button_press(self):
        if self.cola_quantity > 0:
            self._check_for_new_transaction()
            self.check_change_making_ability()
            self.price = 1.00
            self.selected_product = "cola"
            self._button_display()
            self._check_transaction()
        else:
            self.display = "SOLD OUT"

    def chips_button_press(self):
        if self.chips_quantity > 0:
            self._check_for_new_transaction()
            self.check_change_making_ability()
            self.price = 0.50
            self.selected_product = "chips"
            self._button_display()
            self._check_transaction()
        else:
            self.display = "SOLD OUT"

    def candy_button_press(self):
        if self.candy_quantity > 0:
            self._check_for_new_transaction()
            self.check_change_making_ability()
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
            self.balance = round(self.balance, 2)
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
        returning_quarters = 0
        returning_dimes = 0
        returning_nickels = 0
        self.change_due = abs(balance)
        # calculate how many of each coin is needed
        # quarters
        while self.change_due > 0:
            if self.quarter_quantity > 0:
                self.change_due -= 0.25
                # change_due = round(change_due, 2)
                returning_quarters += 1
                self.quarter_quantity -= 1
            else:
                break
        if round(self.change_due, 2) < 0:
            self.change_due += 0.25
            # change_due = round(change_due, 2)
            returning_quarters -= 1
            self.quarter_quantity += 1
        # dimes
        while self.change_due > 0:
            if self.dime_quantity > 0:
                self.change_due -= 0.10
                # change_due = round(change_due, 2)
                returning_dimes += 1
                self.dime_quantity -= 1
            else:
                break
        if round(self.change_due, 2) < 0:
            self.change_due += 0.10
            # change_due = round(change_due, 2)
            returning_dimes -= 1
            self.dime_quantity += 1
        # nickels
        while self.change_due > 0:
            if self.nickel_quantity > 0:
                self.change_due -= 0.05
                # change_due = round(change_due, 2)
                returning_nickels += 1
                self.nickel_quantity -= 1
            else:
                break
        if round(self.change_due, 2) < 0:
            self.change_due += 0.05
            self.change_due = round(self.change_due, 2)
            returning_nickels -= 1
            self.nickel_quantity += 1
        # total
        self.change_due = round(self.change_due, 2)

        # return coins
        for quarter_index in range(returning_quarters):
            self.coin_return.append(quarter)
        for dime_index in range(returning_dimes):
            self.coin_return.append(dime)
        for nickel_index in range(returning_nickels):
            self.coin_return.append(nickel)

    def return_coins(self):
        self.coin_return.extend(self.coins_customer_has_inserted_during_this_transaction)
        for coin in self.coins_customer_has_inserted_during_this_transaction:
            # quarter
            if coin['weight'] == 5.6 and coin['size'] == 24.2:
                self.quarter_quantity -= 1
            # dime
            elif coin['weight'] == 2.2 and coin['size'] == 17.9:
                self.dime_quantity -= 1
            # nickel
            elif coin['weight'] == 5 and coin['size'] == 21.2:
                self.nickel_quantity -= 1
        coin_return_buffer = self.coin_return
        self.new_transaction()
        self.coin_return = coin_return_buffer
        self.coins_customer_has_inserted_during_this_transaction = []
