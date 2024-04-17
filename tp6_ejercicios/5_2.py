def potencia_multiplicando(numeroElevado_A, potencia):
    numero = numeroElevado_A
    while potencia > 1:
        numeroElevado_A *= numero
        potencia -= 1
        print(potencia)
    return numeroElevado_A

print(potencia_multiplicando(4, 3))