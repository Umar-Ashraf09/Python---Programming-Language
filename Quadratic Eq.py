import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
discriminent = (b ** 2) - (4 * a * c)
if discriminent < 0:
    print("There is No Solution")
elif discriminent == 0:
    print("There is One Solution")
    x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print(x)
else:
    x_positive = (b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x_negative = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print("This Equation has Two Solution: ", x_positive, "and", x_negative)
