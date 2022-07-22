
st = input("Enter a string: ")
vowel = set("aeiouAEIOU")
count = 0
for c in st:
    if c in vowel:
        count = count + 1
print("Number of vowels: ", count)