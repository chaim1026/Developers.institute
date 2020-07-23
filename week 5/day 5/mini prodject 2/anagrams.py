from anagram_checker import AnagramChecker

class AnagramProgram(AnagramChecker):
    def menu(self):
        self.choice = (input("please enter a word or (exit) to leave this program:\n").lower())
        return self.choice

    def main(self):
        self.choice = self.menu()
        while self.choice != "exit":
            self.choice = self.choice.lstrip() and self.choice.rstrip()
            if len(self.choice.split()) > 1 or not self.choice.isalpha():
                raise ValueError("you entered more than one word")
            self.valid = self.is_valid_word(self.choice)
            if self.valid:
                self.anagram_list = self.get_anagrams(self.choice)
                print(self)
            else:
                return "not a valid word"
            self.choice = self.menu()

    def __repr__(self):
        return f"YOU WORD: {self.choice}\nthis is a valid english word\nAnagrams for your word: {self.anagram_list}\n"