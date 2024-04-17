numero = int(input("Ingresar dígitos: "))
negativo = 0

if numero < 0:
    numero -= numero * 2
    negativo = 1

numeroInvertido = 0
digito = 0

while numero > 0:
    # obtener ultimo digito
    digito = numero % 10
    print(f"digito: {digito}")
    # agregar digito al numero invertido
    numeroInvertido = (numeroInvertido * 10) + digito
    print(f"numero invertido: {numeroInvertido}")
    # substraer el ultimo digito del numero
    numero //= 10
    print(f"numero: {numero}")
if negativo == 0:
    print(numeroInvertido)
else:
    numeroInvertido -= numeroInvertido * 2
    print(numeroInvertido)




