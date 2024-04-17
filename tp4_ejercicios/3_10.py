number = -1
while number < 0:
    number = int(input("Enter Number: "))
factorial = 1
counter = 1
# 5 * 4 * 3 * 2 * 1
if number > 0:
    while counter != number:
        # counter y factorial se inicializan en 1
        # en cada iteracion, factorial se multiplica por counter + 1 (el numero actual + el que le sigue)
        # luego se suma 1 al counter 
        # cuando counter alcanza a number, entonces se aseguro que se multiplicó todos los nros desde 1 hasta el nro dado se multiplicaron
        factorial *= counter + 1 
        counter += 1
    print(f"Factorial of {number} is: {factorial}")
else:
    print("0 has no factorial")
