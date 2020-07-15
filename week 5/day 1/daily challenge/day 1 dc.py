class Farm():

    def __init__(self, farmer_name):
        self.farmer_name = farmer_name
        self.animals = {}
    
    def add_animal(self, animal, amount = 0):
        i = 1
        if animal not in self.animals:
            self.animals[animal] = amount
            print(self.animals)
        else:
            self.animals[animal] = i + 1
            print(self.animals)

    def get_info(self):
        output = f"{self.farmer_name}'s Farm\n"
        for animal, amount in self.animals.items():
            output += f"{animal}      :{amount}\n"
        output += "    E-I-E-I-O    "
        return output


Macdonald = Farm("macdonald")
Macdonald.add_animal("cow", 5)
Macdonald.add_animal("sheep")
Macdonald.add_animal("sheep")
Macdonald.add_animal("goat", 12)
print(Macdonald.get_info())