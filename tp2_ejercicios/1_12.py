amount = int(input("Enter Amount: "))
bills = [1000, 500, 100, 50, 10, 5, 1]
billAmount = {
    1000: 0,
    500: 0,
    100: 0,
    50: 0,
    10: 0,
    5: 0,
    1: 0
}

for bill in bills:
    if bill == 1:
        billAmount[bill] = amount
    else: 
        billAmount[bill] = amount // bill
        amount %= bill

if billAmount[1000] > 0:
    print(f"'1000' Bill: {billAmount[1000]}")
if billAmount[500] > 0:
    print(f"'500' Bill: {billAmount[500]}")
if billAmount[100] > 0:
    print(f"'100' Bill: {billAmount[100]}")
if billAmount[50] > 0:
    print(f"'50' Bill: {billAmount[50]}")
if billAmount[10] > 0:
    print(f"'10' Bill: {billAmount[10]}")
if billAmount[5] > 0:
    print(f"'5' Bill: {billAmount[10]}")
if billAmount[1] > 0:
    print(f"'1' Bill: {billAmount[1]}")



