class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.__acc_no = acc_no
        self.__name = name
        self.__balance = balance

    def get_acc_no(self):
        return self.__acc_no
    def get_name(self):
        return self.__name
    def get_balance(self):
        return self.__balance

    def set_name(self, name):
        self.__name = name
    def set_balance(self, balance):
        if balance > 0:
            self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount Deposited: ", amount)
        else:
            print("Invalid deposit amount ")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Amount withdrawn: ", amount)
        else:
            print("Insufficient Balance")

    def display(self):
        print("\n--- Account Details---")
        print("Account No: ", self.__acc_no)
        print("Name: ", self.__name)
        print("Balance: ", self.__balance)