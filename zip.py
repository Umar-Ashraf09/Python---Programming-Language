
list1 = ["banana", "apple", "orange"]
count = [3, 4, 5]
price = [0.6, 0.2, 0.7]

for (fruit,counter,prices) in zip(list1,count,price):
    print("I bought " + str(counter) + " " + fruit + "s at " + str(prices) + " $")