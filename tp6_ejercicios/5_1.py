def multiplicar_UsandoSumas(numeroMultiplicar, cantidadVeces):
    numero = 0
    while cantidadVeces != 0:
        numero += numeroMultiplicar
        cantidadVeces -= 1
    return numero

print(multiplicar_UsandoSumas(4, 3))
