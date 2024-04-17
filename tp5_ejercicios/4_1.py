mayores = 0
menores = 0
edad = 0
while edad != -1:
    edad = int(input("Ingresar edad: "))
    if edad > -1 and edad < 18:
        menores += 1
    elif edad > 17 and edad < 101:
        mayores += 1
    else:
        print("Edad Invalida")

total = mayores + menores
promedioMenores = menores * 100 / total
promedioMayores = mayores * 100 / total

print(f"Hay un total de {total} personas en el grupo\n{menores} Menores ({promedioMenores}%)\n{mayores} Mayores ({promedioMayores}%)")