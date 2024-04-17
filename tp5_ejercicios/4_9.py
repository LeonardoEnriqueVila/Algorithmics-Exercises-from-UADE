numero  = -1

while numero < 0:
    numero = int(input("Ingresar número positivo: "))

contador = 0
suma = 0

while contador != numero + 1:
    if contador % 2 != 0:
        suma += contador
        print(contador)
    contador += 1
print(f"Suma: {suma}")    