contador = 0
digitos = int(input("Ingresar dígitos: "))
if digitos < 0:
    digitos += digitos * -2
if digitos == 0:
    contador = 1
elif digitos > -1:
    while digitos != 0:
        digitos //= 10
        contador += 1

print(f"Hay {contador} dígitos")