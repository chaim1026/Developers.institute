# syntax functools.reduce(function, iterable[, initializer])

from functools import reduce

def num_add(a,b):
    return a + b

numbers = [1,2,3,4,5,6,7,8,9]

list_value = reduce(num_add,numbers,100)

print(list_value)

