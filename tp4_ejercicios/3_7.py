i = 1
biggestNum = -float('inf')
biggestIndex = -1
sum = 0
while i < 11:
    number = int(input(f"Enter Number {i}: "))
    sum += number
    if number > biggestNum:
        biggestNum = number
        biggestIndex = i
    i += 1
print(f"Biggest number is: {biggestNum} in position: {biggestIndex}\nAverage: {sum/10}")