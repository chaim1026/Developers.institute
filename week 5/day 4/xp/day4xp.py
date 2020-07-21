from random import randint

def get_words_from_file():
    my_words = []
    with open('day4xp.txt') as f:
        my_words = f.readlines()
    return my_words
    
def get_random_sentence(length):
    word_list = get_words_from_file()
    new_sentence = []
    for i in range(length):
        new_sentence.append(word_list[randint(0,len(word_list))].replace("\n"," "))
    sentence = "".join(new_sentence).lower()
    return sentence

def main():
    length = int(input("how long would you like your sentance to be?(between 2 and 20)!\n"))
    if length >= 2 and length <=20:
        print(get_random_sentence(length))
    else:
        raise ValueError("the number you chose was not between 2 and 20")

main()
