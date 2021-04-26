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

class Checking(Account): #Inheritance

    def __init__(self, filepath, _fee):
        Account.__init__(self, filepath)
        self.fee = _fee

    def transfer(self, amount):
        if self.balance - (amount + self.fee) >= 0:
            self.balance -= (amount + self.fee)
            print("New Balance: $" + str(self.balance) + "!")
        else:
            print("Insufficient funds!")
            print("Current Balance: $" + str(self.balance))


checking = Checking("balance.txt", 5)
checking.deposit(150)
checking.transfer(110)
checking.commit()