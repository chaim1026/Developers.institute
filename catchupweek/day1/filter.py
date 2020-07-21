# syntax filter(function, iterable)

"""letters = ['a','b','d','e','i','j','o']

def filter_vowels(letter):
    vowels = ['a','e','i','o','u']
    if letter in vowels:
        return True
    return False

filtered_vowels = filter(filter_vowels,letters)

print('The filtered vowels are:')
for vowel in filtered_vowels:
    print(vowel)

print(filtered_vowels)"""  

#ask jonathan why 1 prints the place in memory and the other prints the actual answer

letters = ['A','g','L','Z','p']

def cap(letter):
    if letter == letter.upper():
        return True
    return False 

cap_list = filter(cap,letters)

print("the cap letters are:")
for letter in cap_list:
    print(letter)