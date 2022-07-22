inp = input("Enter the number of elements: ")
num = int(inp)

prev_prev = 0
prev = 1
counter = 0

if num <= 0:
    print("Please enter a positive number!")
elif num == 1:
    print(prev_prev)
else:
    print(prev_prev)
    print(prev)

    while counter < num - 2:
        result = prev + prev_prev
        print(result)
        prev_prev = prev
        prev = result
        counter = counter + 1