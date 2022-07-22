import math

#This program is a simple calculator which can add, subtract, multiply, division, exponent and square root.

#Function for addition
def addition(a,b):
    return a + b

#Function for subtraction
def subtraction(a,b):
    return a - b

#Function for multiplication
def multiplication(a,b):
    return a * b

#Function for division
def division(a,b):
    return a / b

#Function for exponent
def exponent(a,b):
    return a ** b

#Function for square root
def radical(a):
    return math.sqrt(a)


while True:
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome!")
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t   Calculator")
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tSelect Functions\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1. Add"
          "\t\t\t2. Subtract\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t3. Multiply\t\t4. Divide"
          "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t5. Exponent\t\t6. Square Root\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t7. Quit")
    operation = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tSelect Any operation (1, 2, 3, 4, 5, 6, 7): ")
    if operation in ("1", "2", "3", "4", "5", "6", "7"):

        #Addition
        if operation == "1":
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tAdd")
            try:
                num1 = int(input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter your First Number: "))
                num2 = int(input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter your Second Number: "))
            except ValueError:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease enter number.")
                continue
            ans = addition(num1,num2)
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tAnswer: " + str(num1), "+", str(num2), "=", str(ans))
            user_input = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter Con to Continue or Q for Quit: ")
            user_input = user_input.lower()
            if user_input == "con":
                continue
            elif user_input == "q":
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tThank You!")
                break
            else:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!")
                break

        #Subtraction
        elif operation == "2":
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tSubtract")
            try:
                num1 = int(input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter your First Number: "))
                num2 = int(input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter your Second Number: "))
            except ValueError:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease enter number.")
                continue
            ans = subtraction(num1,num2)
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tAnswer: " + str(num1), "-", str(num2), "=", str(ans))
            user_input = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter Con to Continue or Q for Quit: ")
            user_input = user_input.lower()
            if user_input == "con":
                continue
            elif user_input == "q":
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tThank You!")
                break
            else:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!")
                break

        #Multiplication
        elif operation == "3":
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tMultiply")
            try:
                num1 = int(input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter your First Number: "))
                num2 = int(input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter your Second Number: "))
            except ValueError:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease enter number.")
                continue
            ans = multiplication(num1,num2)
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tAnswer: " + str(num1), "x", str(num2), "=", str(ans))
            user_input = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter Con to Continue or Q for Quit: ")
            user_input = user_input.lower()
            if user_input == "con":
                continue
            elif user_input == "q":
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tThank You!")
                break
            else:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!")
                break

        #Division
        elif operation == "4":
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tDivide")
            try:
                num1 = int(input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter your First Number: "))
                num2 = int(input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter your Second Number: "))
            except ValueError:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease enter number.")
                continue
            try:
                ans = division(num1, num2)
            except ZeroDivisionError:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Error!\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Zero Division")
                continue
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tAnswer: " + str(num1), "/", str(num2), "=", str(ans))
            user_input = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter Con to Continue or Q for Quit: ")
            user_input = user_input.lower()
            if user_input == "con":
                continue
            elif user_input == "q":
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tThank You!")
                break
            else:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!")
                break

        #Exponent
        elif operation == "5":
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tExponent")
            try:
                num1 = int(input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter your First Number: "))
                num2 = int(input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter your Exponent: "))
            except ValueError:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease enter number.")
                continue
            ans = exponent(num1,num2)
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tAnswer: " + str(num1), "^", str(num2), "=", str(ans))
            user_input = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter Con to Continue or Q for Quit: ")
            user_input = user_input.lower()
            if user_input == "con":
                continue
            elif user_input == "q":
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tThank You!")
                break
            else:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!")
                break

        #Square Root
        elif operation == "6":
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tSquare Root")
            try:
                num1 = int(input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter your Number: "))
            except ValueError:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease enter number.")
                continue
            try:
                ans = radical(num1)
            except ValueError:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  Negative number.")
                continue
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tAnswer: The Square Root of", str(num1), "is: ", str(ans))
            user_input = input("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tEnter Con to Continue or Q for Quit: ")
            user_input = user_input.lower()
            if user_input == "con":
                continue
            elif user_input == "q":
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tThank You!")
                break
            else:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWrong Input!")
                break

        #Quit
        elif operation == "7":
            print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tThank You!")
            break
        break

    else:
        print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tInvalid Operation!\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPlease try again.")

