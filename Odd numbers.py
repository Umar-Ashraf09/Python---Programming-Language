x = int(input("Enter your start number: "))
y = int(input("Enter your end number: "))
for i in range(x, y+1):
    if i % 2 != 0:
        print(i)
