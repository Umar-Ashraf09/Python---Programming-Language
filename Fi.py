x = int(input("Enter number: "))
num1 = 0
num2 = 1
next = 0
for i in range(1,x+1):
    if i == 1:
        print(num1)
    if i == 2:
        print(num2)
    next = num1 + num2
    num1 = num2
    num2 = next
    print(next)