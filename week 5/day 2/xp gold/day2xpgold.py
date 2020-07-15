"""class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


c1 = Bengal("garfield", 5)
c2 = Chartreux("tom",8)
c3 = Siamese("jerry",3)

my_cats = [c1,c2,c3]

my_pets = Pets(my_cats)
my_pets.walk()"""



class BankAccount():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0 and amount == 20 or amount == 50 or amount == 100:
            self.balance += amount
            print(self.balance)
        input1 = input("would you like to make an additional deposit (y/n):")
        if input1 == "y":
            amount = int(input("how much would you like to deposit:"))
            self.deposit(amount)
        return self.balance

    def withdraw(self,amount):
        if amount <= self.balance and amount >= 20 and amount <= 50:
            self.balance -= amount
        return self.balance

class Owner(BankAccount):
    def __init__(self, owner, balance, cc, password):
        super().__init__(owner, balance)
        self.cc = cc
        self.password = password

    def check_owner_info(self, user_cc, user_password):
        for i in range(2):
            if user_password != self.password and i == 0:
                user_password = int(input("Please reenter your password:"))
            elif self.password == user_password:
                return "Would you like to Deposit or to Withdraw?"
            else:
                self.cc = 0
                return "Your credit card has been eaten by the machine!"