from datetime import date 
  
birthdate = input("what is your birthdate dd/mm/yyyy?")
birthdate = birthdate.split("/")
birthdate_list = []
for i in birthdate:
    birthdate_list += [int(i)]
today = date.today() 
day = today.day
month = today.month
year = today.year 
age = year - birthdate_list[2] - ((day, month) < (birthdate_list[0], birthdate_list[1]))
candles = str(age)[-1]
candles = int(candles)
side_cake = int((11 - candles) / 2) * "_"
center_cack = candles * "i"
print(f"    {side_cake}{center_cack}{side_cake}")
print("   |:H:A:P:P:Y:|")
print(" __|___________|__")
print("|^^^^^^^^^^^^^^^^^|")
print("|:B:I:R:T:H:D:A:Y:|")
print("|                 |")
print("~~~~~~~~~~~~~~~~~~~")