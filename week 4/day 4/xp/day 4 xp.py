"""def display_function():
    print("we learned functions")
display_function()"""



"""def favorite_books(title):
    print(f"one of my favorite books is {title}")
favorite_books("sins of the father")"""


"""def make_shirt(size = "large", text = "I love python"):
    print(f"the size is: {size}and text on the shirt is:{text}")
make_shirt()"""



"""m_names = ["david blain", "houdini", "harry potter"]
def show_magicians(names):
    new_list = []
    for name in names:
        name = name + " the great"
        new_list += [name]
    print(new_list)
show_magicians(m_names)"""



"""def describe_city(city_name,country_name = "Israel"):
    print(f"{city_name} is in {country_name}")
describe_city()"""


gender = input("what is your gender answer m or f:")
birthdate = input("what is you r birthdate yyyy/mm/dd:")
current_year = 2020
current_month = 7
current_day = 8
age_list = birthdate.split("/")
year = int(age_list[0])
month = int(age_list[1])
day = int(age_list[2])
def get_age(year, month, day):
    age = current_year - year - ((current_day, current_month) < (day, month))
    return age

def can_retire(gender,age):
    if gender == "m":
        if age >= 67:
            print("congradulations you can retire")
        else:
            print("go back to work")
    else:
        if age >= 62:
            print("congradulations you can retire")
        else:
            print("go back to work")
can_retire(gender, get_age(year, month, day))