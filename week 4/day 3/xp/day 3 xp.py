"""keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dict = zip(keys,values)
print(dict(my_dict))"""



"""store = {
    "name": "Zara",
    "creation_date": 1975 ,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": [{"France": ["blue"]}, {"Spain": ["red"]}, {"US": ["pink", "green"]}]
}
more_on_zara = {
    "creation_date": 1975, 
    "number_stores": 10000
}


store["number_stores"] = 2
clothes_for = store["type_of_clothes"]
print(f"zara makes products for {clothes_for}")
store["country_creation"] = "Spain"
if store["international_competitors"]:
    store["international_competitors"].append("Desigual")
del store["creation_date"]
print(store["international_competitors"][-1])
print(store["major_color"][2])
print(len(store))
print(store.keys())
store.update(more_on_zara)
print(store["number_stores"])
print(store)"""



users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
"""result_1 = {name: users.index(name) for name in users}
result_2 = {users.index(name): name for name in users}
sorted_list = sorted(users)
result_3 = {name: sorted_list.index(name) for name in sorted_list}
print(result_1)
print(result_2)
print(result_3)
result_4 = {name: users.index(name) for name in users if "i" in name and name[0] in ["M", "P"]}
print(result_4)"""

result_5 = {name: number for number, name in enumerate(users)}
print(result_5)