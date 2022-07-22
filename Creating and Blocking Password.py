
user_password = input("Add your password: ")
our_password = user_password
your_answer = ""
number_of_try = 0
number_max_of_try = 5
max_try = "not reached"

while your_answer != our_password and max_try != "reached":
    if number_of_try < number_max_of_try:
        your_answer = input("What is the password? : ")
        number_of_try += 1
    else:
        max_try = "reached"

if max_try == "reached":
    print("Account Blocked!")
else:
    print("Access Granted")
