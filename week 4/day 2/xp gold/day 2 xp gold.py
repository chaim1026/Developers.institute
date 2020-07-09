"""num1 = int(input("please enter a number"))
num2 = int(input("please enter a second number"))
num3 = int(input("please enter a third number"))
numbers = [num1, num2, num3]
biggest = 0
for num in numbers:
    if num > biggest:
        biggest = num
print(f"the greatest number is: {num}")"""



"""alphabet = input("enter a letter of the alphabet")
if(alphabet == "A" or alphabet == "a" or alphabet == "E" or alphabet == "e" or alphabet == "I"
 or alphabet == "i" or alphabet == "O" or alphabet == "o" or alphabet == "U" or alphabet == "u"):
    print(f"{alphabet} is a Vowel")
else:
    print(f"{alphabet} is a Consonant")"""



"""my_list = ["kiwi", "berry", "watermelon", "blueberry", "strawberry"]
print(my_list.index("kiwi"))
print(my_list[0])"""


"""list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
for num in list2:
    list1.append(num)
print(list1)"""


"""import random
num = int(input("please enter a number between 1 to 9:"))
num2 = random.randint(1,10)
if num == num2:
    print("you guessed the number")
else:
    print("you guesed wrong")"""



"""students = [("Tom",19,80), ("John",20,90), ("Jony",17,91), ("Jony",17,93), ("Json",21,85)]
students.sort()
print(students)
"""

menu = {
    "beer": 5,
    "wine": 7,
    "water": 2,
    "coke": 3
}
customer_name = input("Whats the customers name:\n")
waiters_name = input("Whats your name:\n")
name_of_item = input("What item did the customer want:\n")
amount_of_items = int(input("How many items were ordered:\n"))
discount_amount = float(input("What is the discount:\n"))
cost = menu[name_of_item] * amount_of_items
if discount_amount > 0:
    cost = cost * discount_amount
print(f"{customer_name} your total comes out to {cost}")



"""for num in range(1,1000001): 
    print(num)"""



"""numbers = []
sum = 0
for num in range(1,1000001):
    numbers += [num]
    sum += num
print(min(numbers))
print(max(numbers))
print(sum)"""

