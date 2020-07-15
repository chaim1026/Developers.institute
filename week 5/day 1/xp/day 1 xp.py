"""class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat_1 = Cat("garfield", 7)
cat_2 = Cat("tom", 4)
cat_3 = Cat("jerry", 11)

def oldest_cat(*cats):
    biggest = 0
    ages = list(cats)
    for age in ages:
        if age > biggest:
            biggest = age
    print(f"the age of the oldest cat is: {biggest}")

oldest_cat(cat_1.age, cat_2.age, cat_3.age)"""



"""class Dog():

    def __init__(self, name_dog, height_dog):
        self.name = name_dog
        self.height = height_dog

    def talk(self):
        print(f"woof my name is {self.name}")

    def jump(self):
        jump = self.height * 2
        print(f"{self.name}'s' height is {self.height}cm")
    

davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)
davids_dog.talk() 
davids_dog.jump() 
sarahs_dog.talk()    
sarahs_dog.jump()    

def biggest_dog(*dogs):
    dogs = list(dogs)
    biggest_dog = dogs[0]
    for dog in dogs:
        if dog.height > biggest_dog.height:
            biggest_dog = dog
    return biggest_dog

the_biggest_dog = biggest_dog(davids_dog, sarahs_dog)
print(the_biggest_dog.name)

the_biggest_dog.winner = True
print(the_biggest_dog.winner)"""



"""class Song():
    
    def __init__(self,lyrics):
        self.lyrics = lyrics
            

happy_bday = Song(["Have a sunshine on you,","Happy Birthday to you!"])

def sing_me_a_song(self):
        for lyric in self.lyrics:
            print(lyric)

sing_me_a_song(happy_bday)"""



class Zoo():

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []
        self.animals_in_pen = {}

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animals(self, animal_sold):
        print(f"goodbye {animal_sold}")
        self.animals.remove(animal_sold)

    def sort_animals(self):
        i = 1
        self.animals.sort()
        current_letter = self.animals[0][0]
        self.animals_in_pen[i] = []
        for animal in self.animals:
            if animal[0] != current_letter:
                current_letter = animal[0]
                i += 1
                self.animals_in_pen[i] = [animal]
            else:
                self.animals_in_pen[i].append(animal)
        print(self.animals_in_pen)
            

my_zoo = Zoo("biblical zoo")
my_zoo.add_animal("lion")
my_zoo.add_animal("tiger")
my_zoo.add_animal("turtle")
my_zoo.add_animal("zebra")
my_zoo.add_animal("ape")
my_zoo.sort_animals()


