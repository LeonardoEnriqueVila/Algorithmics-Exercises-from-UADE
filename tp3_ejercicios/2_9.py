valid = False
while(valid == False):
    valid = True
    day = int(input("Day: "))
    if day < 1 or day > 31:
        valid = False
    month = int(input("Month: "))
    if month < 1 or month > 12:
        valid = False
    year = int(input("Year: "))
    if year < 0:
        valid = False
    if valid == False:
        print("Invalid Input")

# Primero necesitamos saber si el año es bisiesto para saber si el 29/2 es viable
isLeap = False
if year % 4 == 0: # si es divisible por 4
        if year % 100 == 0: # y es divisible por 100
            if year % 400 == 0: # y es divisible por 400
                isLeap = True
            else: # si es divisible por 4 y por 100, pero no por 400

                isLeap = False
        else: # si es divisible por 4 y no por 100
            isLeap = True
else: # si no es divisible por 4
    isLeap = False

monthSelected = ""
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# checkear que mes es
for i in range(0, 12):
    if month - 1 == i:
        monthSelected = months[i]
        break

# verificar que dias son viables segun el mes
match monthSelected:
    case "January":
        print(f"{day}/{monthSelected}/{year}")
    case "February":
        if day > 29:
            print("Invalid Date")
        elif day == 29 and isLeap == True:
            print(f"{day}/{monthSelected}/{year}")
        elif day == 29 and isLeap == False:
            print("Invalid Date")
        else:
            print(f"{day}/{monthSelected}/{year}")
    case "March":
        print(f"{day}/{monthSelected}/{year}")
    case "April":
        if day > 30:
            print("Invalid Date")
        else:
            print(f"{day}/{monthSelected}/{year}")
    case "May":
        print(f"{day}/{monthSelected}/{year}")
    case "June":
        if day > 30:
            print("Invalid Date")
        else:
            print(f"{day}/{monthSelected}/{year}")
    case "July":
        print(f"{day}/{monthSelected}/{year}")
    case "August":
        print(f"{day}/{monthSelected}/{year}")
    case "September":
        if day > 30:
            print("Invalid Date")
        else:
            print(f"{day}/{monthSelected}/{year}")
    case "October":
        print(f"{day}/{monthSelected}/{year}")
    case "November":
        if day > 30:
            print("Invalid Date")
        else:
            print(f"{day}/{monthSelected}/{year}")
    case "December":
        print(f"{day}/{monthSelected}/{year}")
        




