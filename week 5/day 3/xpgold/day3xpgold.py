class Warrior():
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
        return str(self.lifepoints)