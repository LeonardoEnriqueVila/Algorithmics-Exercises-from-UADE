aprobados = 0
reprobados = 0
aplazados = 0
numeroLegajo = 0

while numeroLegajo != -1:
    numeroLegajo = int(input("Numero de legajo: "))
    if numeroLegajo != -1:
        notaFinal = int(input("Nota final: "))
        if notaFinal > 0 and notaFinal < 11:
            if notaFinal > 3:
                aprobados += 1
            elif notaFinal < 4 and notaFinal > 1:
                reprobados += 1
            else: 
                aplazados += 1
        else:
            print("Nota invalida")
total = aprobados + reprobados + aplazados
porcentajeAplazados = aplazados * 100 / total
print(f"Porcentaje de Aplazados: {porcentajeAplazados}%\nAprobados: {aprobados}\nReprobados: {reprobados}\nAplazados: {aplazados}\nTotal: {total}")