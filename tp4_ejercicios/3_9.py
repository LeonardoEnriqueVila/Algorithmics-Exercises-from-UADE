number = 0
evenCounter = 0
oddCounter = 0
while number != -1:
    number = int(input("Enter Number: "))
    if number != -1:
        if number % 2 == 0:
            evenCounter += 1
        else:
            oddCounter += 1

print(f"Even: {evenCounter}\nOdd: {oddCounter}")