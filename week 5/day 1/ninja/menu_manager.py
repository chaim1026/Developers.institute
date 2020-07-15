class MenuManager():
    def __init__(self,menu):
        self.menu = [
            {"name": "soup", "price": 10, "spice_level": "b", "gluten_index": False},
            {"name": "hamburger", "price": 15, "spice_level": "a", "gluten_index": True},
            {"name": "salad", "price": 18, "spice_level": "a", "gluten_index": False},
            {"name": "french_fries", "price": 5, "spice_level": "c", "gluten_index": False},
            {"name": "beef_bourguignon", "price": 25, "spice_level": "b", "gluten_index": True}
        ]

    def add_item(self,name,price,spice_level,gluten_index):
        key_list = ["name", "price", "spice_level", "gluten_index"]
        info = [name,price,spice_level,gluten_index]
        dish = {}
        for item, info_item in zip(key_list, info):
            dish[item] = info_item
        self.menu.append(dish)

    def update_item(self,name,price,spice_level,gluten_index):
        key_list = ["name", "price", "spice_level", "gluten_index"]
        info = [name,price,spice_level,gluten_index]
        dish2 = {}
        for item, info_item in zip(key_list, info):
            dish2[item] = info_item
        for dish in self.menu:
            if dish["name"] == dish2["name"]:
                dish = dish2
            else:
                print("you have no dish by that name")

    def remove_item(self,name):
        for dish in self.menu:
            if name == dish["name"]:
                self.menu.remove(dish)
            else:
                print("you have no such dish")
