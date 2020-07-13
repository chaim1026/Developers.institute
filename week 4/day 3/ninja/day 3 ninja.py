"""birthdays = {
    "chaim": "1994/10/26",
    "tova": "1996/10/08",
    "shami": "2018/09/05",
    "mosh": "1998/06/17",
    "akiva": "2001/06/25"
}

print("Welcome")
print("You can look up the birthdays of the people in the list!")
name_input = input("please enter a name:\n")
birthday_input = input(f"whats {name_input}'s birthday:\n")
birthdays.update({name_input:birthday_input})
print(birthdays)
name = input("plese enter a persons name:\n")
if name not in birthdays:
    raise TypeError(f"Sorry, we don’t have birthday information for {name}")
print(f"{name}'s birthday is {birthdays[name]}")"""