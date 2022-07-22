print("The Average Counter")
total = 0
count = 0
print("Enetr:- avg for Average or q to Quit")
user_input = input(": ")
user_input = user_input.lower()
if user_input == "avg":
    while True:
        try:
            inp = input("Enter number or Done when you are finish: ")
            inp = inp.lower()
            if inp == "done":
                break
            number = float(inp)
            total = total + number
            count = count + 1
        except ValueError:
            print("Wrong Input!")
        average = total / count
        print("Average: ", average)

elif user_input == "q":
    print("Thank You!")
else:
    print("Wrong Input!")




