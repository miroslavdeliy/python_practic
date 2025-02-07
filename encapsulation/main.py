class BankAccount():
    def __init__(self, start_balance= 0):
        self.__balance = start_balance

    @staticmethod
    def chek_enter():
        check_exit = True
        while check_exit:
            try:
                value = int(input("Введите сумму: "))
                return value
                check_exit = False
            except ValueError:
                print("Введите сумму числом!")


    #Метод внесения депозита
    def make_deposit(self):
        value = self.chek_enter()
        if value > 0:
            self.__balance += value
            print("Депозит пополнен!")
        elif value == 0:
            print("Нельзя пополнить на нулевую сумму!")
        else:
            print("Нельзя пополнить на отрицательную сумму!")

    #Метод снятия денег
    def take_money(self):
        value = self.chek_enter()
        if value > 0 and self.__balance >= value:
            self.__balance -= value
            print("Деньги сняты!")
        elif self.__balance < value:
            print("Недостаточно денег на счете!")
        elif value == 0:
            print("Нельзя снять нулевую сумму!")
        else:
            print("Нельзя снять отрицательную сумму!")

    #Метод проверки баланса
    def check_balance(self):
        return f"Ваш баланс {self.__balance}"


#Основное тело программы
my_account = BankAccount()
check_exit = True
while check_exit:
    print("Введите цифру действия:\n1.Внести депозит\
          \n2.Снять деньги\n3.Показать баланс\n4.Выход")
    user_choice = input()
    if user_choice == "1":
        my_account.make_deposit()
    elif user_choice == "2":
        my_account.take_money()
    elif user_choice == "3":
        print(my_account.check_balance())
    elif user_choice == "4":
        check_exit = False
    else:
        print("Введите только число из списка!")
