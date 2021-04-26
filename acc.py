class Account:

    def __init__(self, filepath):
        self._filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print("New Balance: $" + str(self.balance) + "!")
        else:
            print("Insufficient funds!")
            print("Current Balance: $" + str(self.balance))

    def deposit(self, amount):
        self.balance += amount
        print("New Balance: $" + str(self.balance) + "!")

    def commit(self): 
        with open(self._filepath, 'w') as file:
            file.write(str(self.balance))


account = Account("balance.txt")

account.withdraw(25)
account.deposit(55)
account.withdraw(25)
account.commit()