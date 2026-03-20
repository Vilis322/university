class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            raise ValueError("Баланс не может быть отрицательным!")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return "Депозит был успешно внесён на Ваш счёт."
        elif amount == 0:
            return "Депозит не может быть равен нулю!"
        else:
            return "Депозит не может быть отрицательным!"

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return "Вы успешно сняли средства с Вашего счёта."
        elif amount == 0:
            return "Вы не можете снять сумму, равную нулю!"
        else:
            return "Вы не можете снять сумму, превышающую сумму Вашего баланса!"

    def calculate_rate(self, rate):
        if rate > 0:
            self.__balance += ((self.__balance * rate) / 100)
            return "Процентная ставка успешно начислена."
        elif rate == 0:
            return "Процентная ставка не может быть равна нулю!"
        else:
            return "Процентная ставка не может быть отрицательной!"

    def __str__(self):
        return f"Ваш номер аккаунта: {self.__account_number}. Сумма на Вашем балансе равна: {self.__balance}"


if __name__ == "__main__":

    account_one = BankAccount("123456789", 1000)
    print(account_one)

    account_two = BankAccount("987654321", 1000)
    print(account_two)

    print(account_one.deposit(1000))
    print(account_one)

    print(account_two.deposit(-1000))
    print(account_two)

    print(account_one.withdraw(1500))
    print(account_one)

    print(account_two.withdraw(1500))
    print(account_two)

    try:
        account_one.balance = -1000
    except ValueError as e:
        print(str(e))

    print(account_one.calculate_rate(5))
    print(account_one)
