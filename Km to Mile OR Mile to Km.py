print("Choose ")
print("1. Convert Km to Miles")
print("2. Convert Miles to Km")
while True:
    choice = input("Select one (1 or 2): ")
    if choice in ("1", "2"):
        if choice == "1":
            def Km_to_Miles():
                Km = int(input("Enter your Km: "))
                mile = 0.621371 * Km
                print(Km, "Km", "=", mile, "Miles")
            Km_to_Miles()

        elif choice == "2":
            def Miles_to_Km():
                mile = int(input("Enter your Miles: "))
                Km = mile / 0.621371
                print(mile, "Miles", "=", Km, "Km")
            Miles_to_Km()
        break
    else:
        print("Wrong Input")








