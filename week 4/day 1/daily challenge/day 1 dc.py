import random
string = input("please input a sentance no less then 10 characters")
first = string[0]
print(first)
last = string[-1]
print(last)
sentance = string[0]
print(sentance)
for i in range(1, len(string)):
    sentance += string[i]
    print(sentance)
x = list(string)
random.shuffle(x)
print("".join(x))
    
