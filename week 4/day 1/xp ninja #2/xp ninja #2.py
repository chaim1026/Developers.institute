"""cars_owned = 100
todays_drivers = int(input("how manny drivers are there today\n"))
todays_passengers = int(input("how many passengers are waiting for carpool\n"))
cars_available = cars_owned - todays_drivers
print(f"{cars_owned} cars in total")
print(f"{todays_drivers} drivers registered")
print(f"{cars_available} cars still available")
print(f"{cars_available * 4} available spots left")
print(f"{todays_passengers / todays_drivers} avg passengers per car")"""


"""import re

user_password = input("please enter your password:\n")
x = True

while x:
    if not re.search("[a-z]", user_password):
        break
    elif not re.search("[A-Z]", user_password):
        break
    elif not re.search("[0-9]", user_password):
        break
    elif not re.search("[$#@]", user_password):
        break
    elif not len(user_password) >= 6 and len(user_password) <=12:
        break
    else:
        print("Valid Password")
        x = False

if x:
    print("Not a Valid Password")"""


"""import re

user_name = input("please enter your name (example: John Doe):\n")
user_name_list = user_name.split(" ")
last_name = user_name_list[1]
x = True

while x:
    if not re.search("^[A-Z]", user_name):
        break
    elif not re.search("^[A-Z]", last_name):
        break
    elif not re.search("[a-z]", user_name):
        break
    elif not re.search("[A-Z]", user_name):
        break
    elif not re.search(" {1}", user_name):
        break
    else:
        print("Valid Name")
        x = False

if x:
    print("Not Valid Name")"""