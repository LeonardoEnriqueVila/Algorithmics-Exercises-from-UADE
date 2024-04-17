contadorEmpleados = int(input("Ingresar número de empleados: "))
totalEmpleados = contadorEmpleados
totalSalarios = 0
salariosMayores_200000 = 0
salariosMenores_50000_Categoria3= 0
mayorSalario = 0
legajoGanador = 0
salarioMenor = +float("inf")
totalSalarios_Cat1 = 0
totalSalarios_Cat2 = 0
totalSalarios_Cat3 = 0
salarioPromedio = 0

while contadorEmpleados > 0:
    legajo = int(input("Ingresar legajo: "))


    categoria = -1
    while categoria < 1 or categoria > 3:
        categoria = int(input("Ingresar categoria: "))


    salario = -1
    while salario < 0:
        salario = int(input("Ingresar salario: "))
        totalSalarios += salario
        if salario > 200000:
            salariosMayores_200000 += 1
        elif salario < 50000 and categoria == 3:
            salariosMenores_50000_Categoria3 += 1

        if salario > mayorSalario:
            mayorSalario = salario
            legajoGanador = legajo

        if salario < salarioMenor:
            salarioMenor = salario

        if categoria == 1:
            totalSalarios_Cat1 += salario
        elif categoria == 2:
            totalSalarios_Cat2 += salario
        else:
            totalSalarios_Cat3 += salario
    contadorEmpleados -= 1

salarioPromedio = totalSalarios / totalEmpleados

print(f"Total salarios: {totalSalarios}\nEmpleados que ganan mas de 200k: {salariosMayores_200000}\nEmpleados de categoria 3 que ganan menos de 50k: {salariosMenores_50000_Categoria3}\nLegajo de empleado con mayor sueldo: {legajoGanador}\nSueldo más bajo: {salarioMenor}\nTotal sueldos categoria 1: {totalSalarios_Cat1}\nTotal sueldos categoria 2: {totalSalarios_Cat2}\nTotal sueldos categoria 3: {totalSalarios_Cat3}\nSalario promedio: {salarioPromedio}")