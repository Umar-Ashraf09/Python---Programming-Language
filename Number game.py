def multiply():                                                     #Multiplication calculation function
    user_value_1 = int(input("\t\tEnter the value: "))
    mul = user_value_1 * 5
    print(f"\t\tYour answer: {mul}")

def addition():                                                     #Addition calculation function
    user_value_2 = int(input("\t\tEnter the first digit: "))
    user_value_3 = int(input("\t\tEnter the second digit: "))
    add = user_value_2 + user_value_3
    print(f"\t\tYour answer: {add}")

#Start of Program

print("\t\t\t\t\tWELCOME!")
print("\t\t\t:The Number Guessing Game:")
print("\n\t\t1. For this number enter '!'\t\t6. For this number enter '^'\n\t\t2. For this number enter '@'"
      "\t\t7. For this number enter '&'\n\t\t3. For this number enter '#'\t\t8. For this number enter '*'"
      "\n\t\t4. For this number enter '$'\t\t9. For this number enter '('\n\t\t5. For this number enter '%'")

while True:                                                                #Loop if user selects any number
    choice = input("\t\t\t\t\tChoose the number: ")
    if choice in ("!", "@", "#", "$", "%", "^", "&", "*", "("):
        print("\t\t\t\t//Don't forget the number//")
        print("\n\t\tNow, multiply your number with 5.\n\t\te.g. if you chose 1.\n\t\tThen 1 x 5 = 5.")

        print("\n\t\t//If you want you can multiply here.//")                             #Calc which calls upper func. multiply
        cal_1 = input("\t\tJust type Y to enable Calculator or Press Enter to skip: ")
        if cal_1 == 'Y':
            print("\n\t\t//Calculator//")
            multiply()

        print("\n\t\tNow, separate your result into individual digits (In two digit format). Then add them.\n\t\te.g. if your result is 5.\n\t\tThen 0 + 5 = 5.\n\t\te.g. if your result is 35\n\t\tThen 3 + 5 = 8.")

        print("\n\t\t//If you want you can add here.//")                                  #Calc which valls upper func. addition
        cal_2 = input("\t\tJust type Y to enable Calculator or Press Enter to skip: ")
        if cal_2 == 'Y':
            print("\n\t\t//Calculator//")
            addition()

        print("\n\t\tNow, Enter your result.\n\t\te.g. if your result is 5.\n\t\tThen enter 5.")
        result = int(input("\n\t\tEnter your result: "))                        #Main Guessing Game
        if result == 5:
            print("\n\t\tThe number you choose is: 1")
        elif result == 1:
            print("\n\t\tThe number you choose is: 2")
        elif result == 6:
            print("\n\t\tThe number you choose is: 3")
        elif result == 2:
            print("\n\t\tThe number you choose is: 4")
        elif result == 7:
            print("\n\t\tThe number you choose is: 5")
        elif result == 3:
            print("\n\t\tThe number you choose is: 6")
        elif result == 8:
            print("\n\t\tThe number you choose is: 7")
        elif result == 4:
            print("\n\t\tThe number you choose is: 8")
        elif result == 9:
            print("\n\t\tThe number you choose is: 9")
        else:
            print("\n\t\t!!!Wrong Input!!!")
        break
    else:
        print("\n\t\t!!!Wrong Input!!!\n")

