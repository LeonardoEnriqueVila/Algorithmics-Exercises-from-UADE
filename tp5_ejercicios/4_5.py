dia = 0
mes = 0
año = -1
bisiesto = None
mes_str = None
while año < 0:
    año = int(input("Ingresar año: "))

def calcularBisiesto():
    if año % 4 == 0: # si es divisible por 4
            if año % 100 == 0: # y es divisible por 100
                if año % 400 == 0: # y es divisible por 400
                    bisiesto = "si"
                else: # si es divisible por 4 y por 100, pero no por 400
                    bisiesto = "no"
            else: # si es divisible por 4 y no por 100
                bisiesto = "si"
    else: # si no es divisible por 4
        bisiesto = "no"
    return bisiesto

bisiesto = calcularBisiesto()

while mes < 1 or mes > 12:
    mes = int(input("Ingresar mes: "))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    while dia < 1 or dia > 31:
        dia = int(input("Ingresar día: "))
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    while dia < 1 or dia > 30:
        dia = int(input("Ingresar día: "))
elif mes == 2 and bisiesto == "no":
    while dia < 1 or dia > 28:
        dia = int(input("Ingresar día: "))
elif mes == 2 and bisiesto == "si":
    while dia < 1 or dia > 29:
        dia = int(input("Ingresar día: "))

print(f"Primera fecha: {dia}/{mes}/{año}")

sumarDias = int(input("Sumar días: "))
contador = 0

while sumarDias > 0:
    contador = dia + sumarDias
    if mes > 12:
        año += 1
        bisiesto = calcularBisiesto()
        mes = 1
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if contador > 31:
            sumarDias -= 31 - dia
            mes += 1
            dia = 0
        else:
            sumarDias -= contador
            dia = contador
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if contador > 30:
            sumarDias -= 30 - dia
            mes += 1
            dia = 0
        else:
            sumarDias -= contador
            dia = contador
    elif mes == 2 and bisiesto == "no":
        if contador > 28:
            sumarDias -= 28 - dia
            mes += 1
            dia = 0
        else:
            sumarDias -= contador
            dia = contador
    elif mes == 2 and bisiesto == "si":
        if contador > 29:
            sumarDias -= 29 - dia
            mes += 1
            dia = 0
        else:
            sumarDias -= contador
            dia = contador
    print(f"sumarDias: {sumarDias}, contador: {contador}, dia: {dia}, mes: {mes}" )
    
print(f"Segunda fecha: {dia}/{mes}/{año}")
