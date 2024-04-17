# sueldo
# si es soltero se incrementa un 5% del sueldo por año de antiguedad
# si es casado -> 7%
# Descuentos jubilacion: 11 - obra social: 3 - Sindicato: 3

sueldoBasico = int(input("Sueldo Básico: "))
antiguedad = int(input("Antiguedad: "))
estadoCivil = int(input("Estado civil: "))

incremento = 0
nuevoSueldo = sueldoBasico

if estadoCivil == 1:
    incremento = 5 * antiguedad
    estadoCivil = "Soltero"
else: 
    incremento = 7 * antiguedad
    estadoCivil = "Casado"
incrementoAntiguedad = incremento * sueldoBasico / 100
nuevoSueldo += incrementoAntiguedad

jubilacion = 11 * sueldoBasico / 100
obraSocial = 3 * sueldoBasico / 100
sindicato = 3 * sueldoBasico / 100

nuevoSueldo -= jubilacion + obraSocial + sindicato

print(f"Estado Civil: {estadoCivil}\nSueldo Basico: +{sueldoBasico}\nAntiguedad: {antiguedad} años: +{incrementoAntiguedad}\nJubilacion: -{jubilacion}\nObra Social: -{obraSocial}\nSindicato: -{sindicato}\nSueldo Neto: {nuevoSueldo}")
