P = int(input("Enter the Interest Rate (Format = 5): "))
A = int(input("Enter the Initial Amount of Money: "))
N = int(input("Enter the Amount of Years: "))
Ans = A * (1 + P / 100) ** N
Profit = Ans - A
print("The Total Amount of Invested Money is: ", round(Ans, 3), "and the Profited Money is: ", round(Profit, 3))
