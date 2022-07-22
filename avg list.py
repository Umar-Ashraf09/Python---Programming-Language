
lst = list()
while True:
    inp = input("Enter a number: (Done if finished) ")
    if inp == "done":
        break
    number = float(inp)
    lst.append(number)
average = sum(lst) / len(lst)
print("Average: ", average)