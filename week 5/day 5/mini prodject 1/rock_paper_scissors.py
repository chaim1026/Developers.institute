from game import Game

class Game2(Game):
    def __init__(self, user):
        super().__init__(user)
        self.results = {}

    def get_user_menu_choice(self):
        self.lets_play = input("menu:\n(play) Play new game\n(exit) Show scores and exit\n").lower()
        if self.lets_play == "play" or self.lets_play == "exit":
            return self.lets_play

    def print_results(self):
        return self.results

    def main(self):
        self.lets_play = ""
        while self.lets_play != "exit":
            self.lets_play = self.get_user_menu_choice()
            if self.lets_play == "exit":
                break
            self.result = self.play()
            if self.result in self.results:
                self.results[self.result] += 1
            else:
                self.results[self.result] = 1
        print(self.print_results())
