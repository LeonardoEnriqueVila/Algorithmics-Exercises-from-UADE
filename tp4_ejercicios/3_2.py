finish = 1
numbers = []
while finish == 1:
    number = int(input("Enter Number: "))
    if number == -1:
        finish = -1
    else:
        numbers.append(number)

totalNumbers = len(numbers)
if totalNumbers % 2 == 0:
    print("Even")
else: 
    print("Odd")