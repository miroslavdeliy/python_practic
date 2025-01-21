class BankAccount():
    def __init__(self, value):
        self.__balance = value

    #Метод внесения депозита
    def make_deposit(self, value):
        self.__balance += value

    #Метод снятия денег
    def take_money(self, value):
        self.__balance -= value

    #Метод проверки баланса
    def check_balance(self):
        print(f"Ваш баланс {self.__balance}")


#Основное тело программы
my_account = BankAccount(0)
check_exit = True
while check_exit:
    print("Введите цифру действия:\n1.Внести депозит\
          \n2.Снять деньги\n3.Показать баланс\n4.Выход")
    user_choice = input()
    if user_choice == "1":
        try:
            deposit = int(input("Введите сумму депозита: "))
            my_account.make_deposit(deposit)
        except ValueError:
            print("Введите сумму числом!")
            continue
    elif user_choice == "2":
        try:
            money = int(input("Введите сумму снятия: "))
            my_account.take_money(money)
        except ValueError:
            print("Введите сумму числом!")
            continue
    elif user_choice == "3":
        my_account.check_balance()
    elif user_choice == "4":
        check_exit = False
    else:
        print("Введите только число из списка!")
