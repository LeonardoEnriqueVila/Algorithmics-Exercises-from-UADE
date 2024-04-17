investment = int(input("Enter Initial Investment: "))
originalInvestment = investment
numberOfMonths = int(input("Enter total months to know profit: "))
for i in range(1, numberOfMonths + 1):
    profit = 2 * investment / 100
    investment += profit
    print(f"Month {i} amount: {investment:.2f} -> Profit: {profit:.2f}")

print(f"After {numberOfMonths} months profit will be: {investment - originalInvestment:.2f}")



