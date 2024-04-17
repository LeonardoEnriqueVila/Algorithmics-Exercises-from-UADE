finish = 1
largest = float('-inf')
lowest = float('inf') 
while finish == 1:
    number = int(input("Enter Number: "))
    if number == -1:
        finish = -1
    else:
        if number > largest:
            largest = number
        elif number < lowest:
            lowest = number

print(f"Lowest: {lowest}\nLargest: {largest}")