
product_name_1 = input("What is the name of product 1: ")
product_name_1 = product_name_1.capitalize()
product_price_1 = input(f"What is the price of {product_name_1}: ")
product_quantity_1 = input(f"What is the quantity of {product_name_1}: ")

product_name_2 = input("What is the name of product 2: ")
product_name_2 = product_name_2.capitalize()
product_price_2 = input(f"What is the price of {product_name_2}: ")
product_quantity_2 = input(f"What is the quantity of {product_name_2}: ")

product_name_3 = input("What is the name of product 3: ")
product_name_3 = product_name_3.capitalize()
product_price_3 = input(f"What is the price of {product_name_3}: ")
product_quantity_3 = input(f"What is the quantity of {product_name_3}: ")


result_1 = float(product_price_1) * float(product_quantity_1)
result_2 = float(product_price_2) * float(product_quantity_2)
result_3 = float(product_price_3) * float(product_quantity_3)
sum = result_1 + result_2 + result_3

tax = input("What is Tax percentage: ")
tax_addition = sum + (sum * (float(tax) / 100))

dis = input("What is Discount percentage: ")
discount = tax_addition - (tax_addition * (float(dis) / 100))


print("\n\t\t\t\t\t\tSR.NO.\t\t\t\tNAME\t\t\t\tPRICE\t\t\t\tQUANTITY\t\t\t\tTOTAL PRICE")
print(f"\n\t\t\t\t\t\t1.\t\t\t\t\t{product_name_1}\t\t\t\t{product_price_1}\t\t\t\t\t{product_quantity_1}\t\t\t\t\t\t{result_1}")
print(f"\n\t\t\t\t\t\t2.\t\t\t\t\t{product_name_2}\t\t\t\t{product_price_2}\t\t\t\t\t{product_quantity_2}\t\t\t\t\t\t{result_2}")
print(f"\n\t\t\t\t\t\t3.\t\t\t\t\t{product_name_3}\t\t\t\t{product_price_3}\t\t\t\t\t{product_quantity_3}\t\t\t\t\t\t{result_3}")
print(f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTOTAL\t\t\t\t\t{sum}")
print(f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTax\t\t\t\t\t\t{tax}%")
print(f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tDiscount\t\t\t\t{dis}%")
print(f"\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tNET AMOUNT\t\t\t\t{discount}")

