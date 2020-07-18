from random import randint

def get_words_from_file():
    my_words = []
    with open('day4xp.txt') as f:
        for line in f.readlines():
            my_words.append(line)
    return my_words
    
def get_random_sentence(length):
    word_list = get_words_from_file()
    new_sentence = []
    resetting = []
    for i in range(length):
        new_sentence.append(word_list[randint(0,len(word_list))])
    for word in new_sentence:
        resetting.append(word.replace("\n"," "))
    sentence = "".join(resetting).lower()
    return sentence

def main():
    length = int(input("how long would you like your sentance to be?(between 2 and 20)!\n"))
    if length >= 2 and length <=20:
        print(get_random_sentence(length))
    else:
        raise ValueError("the number you scose was not between 2 and 20")

main()
