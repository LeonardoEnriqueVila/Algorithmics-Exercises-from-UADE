investments = []
totalInvestment = 0
for i in range(1, 4):
    investment = int(input(f"Person {i} investment: "))
    investments.append(investment)
    totalInvestment += investment
    
for i in range(1, 4):
    percentageInvestment = investments[i - 1] * 100 / totalInvestment
    print(f"Person {i} invested: {percentageInvestment:.2f}%")