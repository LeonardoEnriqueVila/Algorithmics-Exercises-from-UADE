numero = int(input("ingresar un numero para FIBONACCI: "))
# necesito saber cuantos nros hay en esa sucecion para saber cuantos numbersRead puede haber
Nterminos = int(input("Ingresar N primeros terminos de esa sucesion: "))

sum = 1
contador = 2
primero = 0
print(primero)
segundo = 1
print(segundo)
tercero = -1

while tercero != numero and contador < Nterminos:
    tercero = primero + segundo
    sum += tercero
    #print(f"{primero}, {segundo}, {tercero}")
    print(tercero)
    primero = segundo
    segundo = tercero
    contador += 1
print(f"Suma: {sum}")

"""
0 1 1  
  1 1 2 
    1 2 3                      
      2 3 5

# primero (0) + segundo (1) = tercero (1)

# primero = segundo
# segundo = tercero
# tercero = primero + segundo
"""