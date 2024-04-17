a = int(input("Enter number 'A': "))
b = int(input("Enter number 'B': "))
sum = a + b
dif = 0
if a > b:
    dif = a - b
else:
    dif = b - a
print(f"Sum: {a} + {b} = {sum}\nDif = {dif}")
