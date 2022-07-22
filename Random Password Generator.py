import random
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()?/\-=_+|][}{><;:0123456789"
length = int(input("Length of password: "))
password = ""
for i in range(length):
    password += random.choice(chars)
print(f"Your password is : {password}")