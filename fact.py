
inp = input("Enter the first number: ")
num = int(inp)
fact = 1
if num < 0:
    print("Factorial doesn't exists!")
elif num == 0:
    print("The Factorial of 0! is 1.")
else:
    for i in range(1,num+1):
        fact = fact * i
    print(f"The Factorial of {num} is: {fact}")
