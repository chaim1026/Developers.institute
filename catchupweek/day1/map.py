# syntax map(function, iterable, ...)

"""class Calculate():
    def __init__(self,numbers):
        self.numbers = numbers
        self.result = map(self.calculate_square,self.numbers)
        self.number_square = set(self.result)

    def calculate_square(self, n):
        return n*n

    def get_info(self):
        return self.number_square"""


def cap(letter):
    return letter.upper()

result = list(map(cap, "abc"))
print(result)
