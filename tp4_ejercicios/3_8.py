numberCounter = 0
sum = 0
while sum <= 101:
    number = int(input("Enter Number: "))
    numberCounter += 1
    if number % 2 == 0:
        sum += number
print(f"The sum of the even numbers is {sum} -> A total of {numberCounter} were given")