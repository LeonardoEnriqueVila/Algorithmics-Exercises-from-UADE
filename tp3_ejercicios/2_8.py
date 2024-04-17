# bisiesto si es divisible por 4
# si es divisible por 4 y por 100 no es bisiesto a menos que sea divisible por 400

while True:
    year = int(input("Enter Year: "))
    if year % 4 == 0: # si es divisible por 4
        if year % 100 == 0: # y es divisible por 100
            if year % 400 == 0: # y es divisible por 400
                print(f"{year} is a leap year")
            else: # si es divisible por 4 y por 100, pero no por 400
                print(f"{year} is NOT a leap year")
        else: # si es divisible por 4 y no por 100
            print(f"{year} is a leap year")
    else: # si no es divisible por 4
        print(f"{year} is NOT a leap year")
