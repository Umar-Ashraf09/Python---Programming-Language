x = int(input("Enter your start number: "))
y = int(input("Enter your end number: "))
print("The prime numbers between", x, "and", y, "are: ")
for num in range(x, y+1):
    if num > 1:
        for i in range(2, num):
            if num%i == 0:
                break
        else:
            print(num)
