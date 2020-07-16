class Palindrome():
    def __init__(self,word):
        self.word = word
        self.word_list = []

    """def sort(self):
        for letter in self.word:
            self.word_list.append(letter)
        self.word_list.reverse()
        self.new_word = "".join(self.word_list)
        print(self.new_word)
        return self.new_word"""

    def sort(self):
        self.reverse = self.word[::-1]
        print(self.reverse)
        return self.reverse

    def check_palindrome(self):
        if self.sort() == self.word:
            print(True)
        else:
            print(False)

    def __repr__(self):
        return f"your new word is {self.reverse}"
