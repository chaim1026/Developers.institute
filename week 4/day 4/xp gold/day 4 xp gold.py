"""import random
def get_random_temp(season):
    if season == "summer":
        random_num = random.randint(28,40)
    elif season == "fall":
        random_num = random.randint(15,27)
    elif season == "winter":
        random_num = random.randint(-10,15)
    else:
        random_num = random.randint(15,27)
    return random_num

def main():
    season = input("please enter a season:\n")
    temp = get_random_temp(season)
    print(f"the temp is {temp}")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif temp >= 0 and temp < 16:
        print("Quite chilly! Don’t forget your coat")
    elif temp >= 16 and temp <= 23:
        print("going to be a bit chilly today")
    elif temp >= 24 and temp < 32:
        print("perfect weather not to hot and not cold enjoy")
    else:
        print("its hot today enjoy the weather")
main()"""



import random
def throw_dice():
    num = random.randint(1,6)
    return num

def throw_until_doubles():
    first_die = random.randint(1,6)
    second_die = random.randint(1,6)
    i = 1
    while first_die != second_die:
        first_die = throw_dice()
        second_die = throw_dice()
        i += 1
    return i


def main():
    total_throws = 0
    for i in range(101):
        total_throws += throw_until_doubles()
        avg = total_throws / 100
    print(f"total throws: {total_throws}\naverage is: {avg}")
main()
    