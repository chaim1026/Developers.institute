"""class Warrior():
    def __init__(self,character_name,lifepoints = 50):
        self.character = character_name
        self.lifepoints = lifepoints
        print("Grrr..")

    def roar(self):
        print(self.character)

    def attack(self,other_player):
        other_player.lifepoints -= 10
        return other_player.lifepoints

    def __repr__(self):
        return f"{self.character} is screaming realy loud!!!"
        

class Sorcerer():
    def __init__(self,character_name,lifepoints = 50):
        self.character = character_name
        self.lifepoints = lifepoints
        print("Wooba lubba dub dub")

    def curse(self):
        print(self.character)

    def __repr__(self):
        return f"{self.character} is pronounceing a scary curse"

class Drood():
    def __init__(self,character_name,lifepoints = 50):
        self.character = character_name
        self.lifepoints = lifepoints
        print("hello world")

    def heal(self):
        self.lifepoints += 10
        return self.lifepoints

    def heal_other(self,other_player):
        other_player.lifepoints += 10
        return other_player.lifepoints

    def __repr__(self):
        return str(self.lifepoints)"""




number = int(input("please enter a number between 1 - 100\n"))

def outer_function(number):

    def wrapper(*args):
        print("you entered a number now lets ses the outcome")
        return number(*args)
    return wrapper


@outer_function
def bigger(number):
    if number > 50:
        return True
    return False

@outer_function
def lower(number):
    if number < 50:
        return True
    return False

@outer_function
def equal(number):
    if number == 50:
        return True
    return False

