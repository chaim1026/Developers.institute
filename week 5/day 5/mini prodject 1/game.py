from random import choice

class Game():
    def __init__(self, user):
        self.user = user

    def get_user_item(self):
        self.choice = input("(r) Rock\n(p) Paper\n(s) Scissors\n").lower()
        while self.choice != "r" and self.choice != "p" and self.choice != "s":
            self.choice = input("(r) Rock\n(p) Paper\n(s) Scissors\n").lower()
        return self.choice   
        
    def get_computer_item(self):
        self.computer_choice = choice(["r", "p", "s"])
        return self.computer_choice

    def get_game_result(self,choice,computer_choice):
        if choice == "r" and computer_choice == "r":
            return "draw"
        elif choice == "r" and computer_choice == "p":
            return "loss"
        elif choice == "r" and computer_choice == "s":
            return "win"
        elif choice == "p" and computer_choice == "p":
            return "draw"
        elif choice == "p" and computer_choice == "s":
            return "loss"
        elif choice == "p" and computer_choice == "r":
            return "win"
        elif choice == "s" and computer_choice == "s":
            return "draw"
        elif choice == "s" and computer_choice == "r":
            return "loss"
        else:
            return "win"

    def play(self):
        self.user_item = self.get_user_item()
        self.computer_item = self.get_computer_item()
        self.outcome = self.get_game_result(self.user_item,self.computer_item)
        print(f"{self.user} selected {self.user_item}.\nThe computer selected {self.computer_item}.\nThe result is: {self.outcome}")
        return self.outcome
