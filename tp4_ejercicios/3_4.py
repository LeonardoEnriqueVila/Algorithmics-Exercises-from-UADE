sum = 0
for i in range(42, 177):
    if i % 2 != 0:
        sum += i
        print(i)
print(f"Sum is {sum}")