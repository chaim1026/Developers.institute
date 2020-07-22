class AnagramChecker():
    def __init__(self):
        self.fixed_word_list = []
        with open("words.txt") as f:
            self.words = f.readlines()
            for word in self.words:
                self.new_word = word.replace("\n","").lower()
                self.fixed_word_list.append(self.new_word)

    def is_valid_word(self,user_word):
        self.user_word = user_word
        if self.user_word in self.fixed_word_list:
            return True
        return False

    def get_anagrams(self,user_word):
        self.anagrams = []
        self.sorted_word = sorted(self.user_word)
        self.new_word = "".join(self.sorted_word)
        for word in self.fixed_word_list:
            self.sorted_word2 = sorted(word)
            self.new_word2 = "".join(self.sorted_word2)
            if self.new_word == self.new_word2:
                self.anagrams.append(word)
        return self.anagrams


        
   