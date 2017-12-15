items = [1, 2, 3, 4, 5]

#Map
squared = list(map(lambda x: x*2, items))

def multiply(x):
    return (x*x)

def add(x):
    return (x+x)

funcs = [multiply, add]

for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print value

#Filter

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))

print less_than_zero


list = [1, 2, 3, 4]

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print product

