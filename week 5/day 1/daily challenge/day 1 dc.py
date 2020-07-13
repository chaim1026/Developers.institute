class Farm():

    def __init__(self, farmer_name):
        self.farmer_name = farmer_name
        self.animals = {}
    
    def add_animal(self, animal, amount = 0):
        i = 1
        if animal not in self.animals:
            self.animals[animal] = amount
        else:
            self.animals[animal] = i + 1

    def get_info(self):
        



macdonald = Farm("macdonald")
macdonald.add_animal("cow", 5)
macdonald.add_animal("sheep")
macdonald.add_animal("sheep")
macdonald.add_animal("goat", 12)
macdonald.get_animals()