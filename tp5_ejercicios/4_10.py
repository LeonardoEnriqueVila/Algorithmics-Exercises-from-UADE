espectadores = 1
espectadores_descuento = 0
espectadores_SIN_descuento = 0
recaudacion = 0

while espectadores != 0:
    espectadores = int(input("Cantidad de expectadores: "))
    if espectadores != 0:
        descuento = int(input("Ingresar si tiene descuento 1(SI) - 2(NO): "))
        if descuento == 1:
            espectadores_descuento += espectadores
        elif descuento == 2:
            espectadores_SIN_descuento += espectadores

recaudacion = (espectadores_descuento * 3500) + (espectadores_SIN_descuento * 5000)

print(f"La recaudación es de: {recaudacion}\nEspectadores con descuento: {espectadores_descuento}\nPorcentaje espectadores con descuento: {espectadores_descuento * 100 / (espectadores_descuento + espectadores_SIN_descuento)}")

