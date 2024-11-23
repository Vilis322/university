def xyz(amount):
    try:
        amount = float(amount)

        currency_before_exchange = input("What name of currency you have?\n")
        currency_after_exchange = input("What name of currency you wanna buy?\n")

        if currency_before_exchange == "dollar" and currency_after_exchange == "euro":
            result = float(amount) / 1.17
            return print(result)

        elif currency_before_exchange == "euro" and currency_after_exchange == "dollar":
            result = float(amount) * 1.17
            return print(result)

        else:
            return print(ValueError("We can exchange only dollar and euro"))
    except ValueError as e:
        print("You did a mistake!!! You have to write only number!!!")
        print(str(e))


amount_of_money = input("How much money do you want to change?\n")

print(xyz(amount_of_money))
