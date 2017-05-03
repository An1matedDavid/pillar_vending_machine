__author__ = 'MrJ'


class VendingMachine:

    current_amount = 0
    coin_return = []
    display = "INSERT COIN"

    def vending_machine_reset(self):
        self.current_amount = 0
        self.coin_return = []
        self.display = "INSERT COIN"

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
            self.current_amount += 25
        # dime
        elif coin['weight'] == 2.2 and coin['size'] == 17.9:
            self.current_amount += 10
        # nickel
        elif coin['weight'] == 5 and coin['size'] == 21.2:
            self.current_amount += 5
