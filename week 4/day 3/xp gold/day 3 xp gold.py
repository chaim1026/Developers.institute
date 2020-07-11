"""fruits = input("please enter your favorite fruits separate them with a space:\n")
fruits = fruits.split(" ")
new_fruit = input("please input 1 fruit:\n")
for fruit in fruits:
    if fruit == new_fruit:
        print("you chose one of your favorite fruits enjoy")
        break
    else:
        print("You chose a new fruit. I hope you enjoy it")
        break"""



"""car_manufacturers = "Honda, Volkswagen, Toyota, Ford_motor, Honda, Chevrolet"
car_manufacturers = car_manufacturers.split(", ")
length = len(car_manufacturers)
print(f"you have {length} car manufacturers in your list")
car_manufacturers.sort(reverse = True)
print(car_manufacturers)
o = 0
i = 0
for cars in car_manufacturers:
    for letter in cars:
        if letter == "o":
            o += 1
            break
    for letter in cars:
        if letter == "i":
            i += 1
            break
i = length - i
print(f"there are {o} car manufacturers with the letter o in them and {i} car manufacturers without the letter i in them")
car_manufacturers = list(dict.fromkeys(car_manufacturers))
print(car_manufacturers)"""



"""my_list = ["kiwi", "apple", "pineapple", "orange"]
my_list.insert(2, "grapes")
print(my_list)"""



"""string = "hey my name id chaim wiesner"
num = string.count(" ")
print(num)"""


string = "Hey my name is Chaim Wiesner"
upper = 0
lower = 0
for letter in string:
    if letter.isupper():
        upper += 1
    elif letter.islower():
        lower += 1
print(upper)
print(lower)

