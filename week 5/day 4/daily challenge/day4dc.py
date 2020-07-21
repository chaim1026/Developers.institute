import string
import nltk
from nltk.corpus import stopwords
import re

class Text():

    def __init__(self,string):
        self.string = string
        self.word_list = self.string.split()

    def word_frequency(self,word_check):
        i = 0
        for word in self.word_list:
            if word == word_check:
                i += 1
        if i > 0:
            return i
        return None

    def most_common_word(self):
        self.word_dict = {}
        self.most_used_word = ""
        times_used = 0
        for word in self.word_list:
            if word in self.word_dict:
                self.word_dict[word] = self.word_dict[word] + 1
            else:
                self.word_dict[word] = 1
        for item in self.word_dict.items():
            if item[1] > times_used:
                times_used = item[1]
                self.most_used_word = item[0]
        return self.most_used_word

    def all_unique_words(self):
        self.unique_word_list = list(set(self.word_list))
        print(self.unique_word_list)

    @classmethod
    def text_file(cls, file):
        with open(file, "r") as f:
            file_string = str(f.read().replace("\n", " "))
        return cls(file_string)

    
class TextModification(Text):
    def no_punctuation(self):
        for i in self.string:
            if i in string.punctuation:
                self.string = self.string.replace(i,"")

        return self.string
    
    """translation_table = str.maketrans('', '', string.punctuation)
        return ''.join([letter.translate(translation_table) for letter in self.string])"""

    def no_stop_words(self):
        en_stops = set(stopwords.words("english"))
        for word in self.word_list:
            if word in en_stops:
                self.word_list.remove(word)
        return " ".join(self.word_list)

    def no_special_characters(self):
        for i in self.string.split("\n"):
            return re.sub(r"[^a-zA-Z0-9]+"," ",i)
