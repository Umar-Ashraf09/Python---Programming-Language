                  #This simple program takes input from the user to divide bill between them.
        #The user have to give names of the people (this program is capable of calculating from 3 user input).
    #Here the program only works on food as pizza. Number of pizzas, price of pizza and number of slices of pizza.
                #Then divides the price upon number of slices to calculate price for each person.


            #Function to print final solution. Final solution are going to be checked for to condition.
                                  #Therefore, created a function for that.
def final_result():
    result_1 = float(number_of_slice_1_ate) * float(each_slice_price)
    result_2 = float(number_of_slice_2_ate) * float(each_slice_price)
    result_3 = float(number_of_slice_3_ate) * float(each_slice_price)

    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tFirst person " + name_1 + " have to pay: " + str(result_1))
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tSecond person " + name_2 + " have to pay: " + str(result_2))
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tThird Person " + name_3 + " have to pay: " + str(result_3))


#Input from user
name_1 = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tWhat is the name of first person?: ")
name_2 = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tWhat is the name of second person?: ")
name_3 = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tWhat is the name of third person?: ")


                                             #main calculation
number_of_pizza = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tHow many pizza(s) were ordered?: ")
pizza_price = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tWhat is the price of one pizza?: ")
pizza_slice = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tHow many slice one pizza have?: ")
total_slices = float(number_of_pizza) * float(pizza_slice)
print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tSo, total number of slices are: " + str(total_slices))
each_slice_price = float(pizza_price) / float(total_slices)


                           #Input from user to take each person's pizza slice intake
number_of_slice_1_ate = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tHow many slice do " + name_1 + " ate?: ")
number_of_slice_2_ate = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tHow many slice do " + name_2 + " ate?: ")
number_of_slice_3_ate = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tHow many slice do " + name_3 + " ate?: ")
leftover = total_slices - (float(number_of_slice_1_ate) + float(number_of_slice_2_ate) + float(number_of_slice_3_ate))


                                 #Condition to check leftover pizza slices
if leftover == 0:
    print(f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tNumber of slices left is 0")
    final_result()
elif leftover > 0:
    print(f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tNumber of slices left is {leftover}")
    final_result()
else:
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!")
