"""class Currency():
    def __init__(self,value,currency):
        self.value = float(value)
        self.currency = currency

    def __repr__(self):
        return f"you have {self.value}{self.currency}"

    def __str__(self):
        return f"you have {self.value}{self.currency}"

    def __int__(self):
        return int(self.value)

    def __add__(self,another_currency):
        if self.currency == another_currency:
            self.value += 5
            return self.value
        else:
            raise ValueError("not the same currency")

    def __iadd__(self,another_currency):
        if self.currency == another_currency:
            self.value += 5
            return self.value
        else:
            raise ValueError("not the same currency")

    def __sub__(self,another_currency):
        if self.currency == another_currency:
            self.value -= 5
            return self.value
        else:
            raise ValueError("not the same currency")

    def __isub__(self,another_currency):
        if self.currency == another_currency:
            self.value -= 5
            return self.value
        else:
            raise ValueError("not the same currency")

    def __mul__(self,another_currency):
        if self.currency == another_currency:
            self.value *= 5
            return self.value
        else:
            raise ValueError("not the same currency")

    def __imul__(self,another_currency):
        if self.currency == another_currency:
            self.value *= 5
            return self.value
        else:
            raise ValueError("not the same currency")

    def __div__(self,another_currency):
        if self.currency == another_currency:
            self.value /= 5
            return self.value
        else:
            raise ValueError("not the same currency")

    def __idiv__(self,another_currency):
        if self.currency == another_currency:
            self.value /= 5
            return self.value
        else:
            raise ValueError("not the same currency")"""



"""import math
class Circle():
    pi = math.pi

    def __init__(self,radius):
        self.radius = radius
        self.perimeter = Circle.pi * (2 * self.radius)
        self.area = Circle.pi * (self.radius ** 2)

    def __repr__(self):
        return f"the area in your circle is: {self.area} and the perimeter is: {self.perimeter}"

    def __add__(self,other_circle):
        both_circles = self.area + other_circle.area
        return both_circles

    def __gt__(self,other_circle):
        if int(self.area) > int(other_circle.area):
            return True
        return False 

    def __eq__(self,other_circle):
        if self.area == other_circle.area:
            return True
        return False 

def sort(*circles):
    circle_list = []
    for circle in circles:
        circle_list.append(circle)
    circle_list.sort()
    return circle_list"""



