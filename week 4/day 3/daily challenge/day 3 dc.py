users_string = input("please enter a sentance:")
action = input("please choose encrypt or decrypt:")
letter_list = []
outcome = ""
if action == "encrypt":
    for letter in users_string:
        if letter != " ":
            letter_list += [ord(letter) + 3]
        else:
            letter_list += [ord(letter)]
    for num in letter_list:
        outcome += chr(num)
    print(outcome)
else:
    for letter in users_string:
        if letter != " ":
            letter_list += [ord(letter) - 3]
        else:
            letter_list += [ord(letter)]
    for num in letter_list:
        outcome += chr(num)
    print(outcome)