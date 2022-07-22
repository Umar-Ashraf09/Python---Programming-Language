import math
def cosine(x):
    cosine_x = 1 - (x ** 2 / math.factorial(2)) + (x ** 4 / math.factorial(4)) - (x ** 6 / math.factorial(6)) + (x ** 8 / math.factorial(8)) - (x ** 10 / math.factorial(10))
    print(cosine_x)

cosine(math.pi/6)
