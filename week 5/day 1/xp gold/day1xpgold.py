"""import math

class Circle():
    pi = math.pi

    def __init__(self, radius = 1.0):
        self.radius = radius

    def perimeter(self):
        perimeter = Circle.pi * (2 * self.radius)
        return perimeter

    def area(self):
        area = Circle.pi * (self.radius ** 2)
        return area

    def get_info(self):
        print(self.perimeter())
        print(self.area())




math = Circle(3)
math.perimeter()
math.get_info()"""

"""
import random

class MyList():
    pass

    def __init__(self,list1):
        self.list1 = list1

    def reversed_list(self):
        self.list1.sort(reverse = True)

    def sorted_list(self):
        self.list1.sort()

    def random_list(self):
        list2 = [random.randint(1, 25) for num in range(len(self.list1))]
        print(list2)


my_list = MyList([5, 9, 7, 2, 3, 4, 12, 1])
my_list.random_list()"""


import random

class QuantumParticle():

    def __init__(self):
        self.position = random.randint(1, 10000)
        self.momentum = random.random()
        self.spin = random.choice([0.5, -0.5])

    def get_position(self):
        current_position = self.position
        self.disturbance()
        return current_position
    
    def get_momentum(self):
        current_momentum = self.momentum
        self.disturbance()
        return current_momentum

    def get_spin(self):
        self.spin = random.choice([0.5, -0.5])
        return self.spin

    def disturbance(self):
        self.position = random.randint(1, 10000)
        self.momentum = random.random()

    def __repr__(self):
        return f"your position is: {self.position} your momentum is: {self.momentum}"
    
