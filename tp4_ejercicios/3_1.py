finish = 1
numbers = []
iterations = -1
while finish == 1:
    number = int(input("Enter Number: "))
    if number == -1:
        finish = -1
    else:
        iterations += 1
        numbers.append(number)
print(f"First Number is {numbers[0]}\nLast Number is {numbers[iterations]}")