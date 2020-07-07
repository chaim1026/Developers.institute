"""my_fav_numbers = set([7,1])
my_fav_numbers.add(9)
my_fav_numbers.add(5)
my_fav_numbers.remove(5)
print(my_fav_numbers)
friend_fav_numbers = set([2,8])
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)"""



"""float can have a desimal point an int cant
yes you can use a list
num = 1
while num < 5:
    num += 0.5
    print(num)"""


"""for i in range(1,21):
    print(i)"""


"""active = True
while active:
    topping = input("please choose a pizza topping(enter quit when you are finished):")
    if topping == "quit":
        active = False
    else:
        print("will add that to your pizza")  """  


"""sum = 0
while True:
    age = input("please enter your ages (when you finish enter quit)")

    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        continue
    elif age >= 3 and age <= 12:
        cost = 10
        sum += cost
    elif age > 12:
        cost = 15
        sum += cost
print(f"your cost is {sum}$")"""

"""allowed = []
while True:
    age = input("please enter your age (when you are finished enter quit):")

    if age == 'quit':
        break

    age = int(age)
    if age < 21:
        continue
    else:
        allowed += [str(age)]

", ".join(allowed)
print(f"{allowed} can watch the movie")"""


"""names = ["chaim", "zev", "shami", "tova", "mosh", "akiva"]
new_names = ["chaim", "zev", "shami", "tova", "mosh", "akiva"]
for name in names:
    age = int(input(f"{name} what is your age?"))
    if age <= 16:
        new_names.remove(name)
print(new_names)"""


"""basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0,"Apples")
apples = basket.count("Apples")
print(f"you have {apples} Apples")
while basket:
    basket.pop()
print(basket)"""

"""your_list = input("write your list here")
your_list = list(your_list.split(" "))
i = 0
n = -1
while i < len(your_list):
    print(your_list[n])
    n -= 1
    i += 1 """


"""your_list = input("write your list here")
your_list = list(your_list.split(" "))
i = 0
while i < len(your_list):
    if i % 2 == 0:
        print(your_list[i])
    i += 1"""

"""n = 3
my_list = []
for multiply in range(1,11):
    my_list.append(n * multiply)
print(my_list)"""


"""for num in range(1500,2701):
    if num % 7 == 0 and num % 5 == 0:
        print(num)"""