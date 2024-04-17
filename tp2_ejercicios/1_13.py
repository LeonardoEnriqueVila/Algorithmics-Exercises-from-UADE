# obtener nro binario de 4 cifras - que solo tenga 0s y 1s
approved = False
while (approved == False):
    approved = True
    binaryNumber = input("Enter 4 digit Binary Number: ")
    if len(binaryNumber) != 4:
        print("Binary Number must be size 4")
        approved = False
        break
    for i in range(0, 4):
        if binaryNumber[i] == "1" or binaryNumber[i] == "0":
            approved = True
        else: 
            print("Its not a Binary Number")
            approved = False
            break
# pasar a binario 
sum = 0
if binaryNumber[3] == "1":
    sum += 2 ** 0
if binaryNumber[2] == "1":
    sum += 2 ** 1
if binaryNumber[1] == "1":
    sum += 2 ** 2
if binaryNumber[0] == "1":
    sum += 2 ** 3

print(f"Number is: {sum}")