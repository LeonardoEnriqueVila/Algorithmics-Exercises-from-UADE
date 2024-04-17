number = -1
while number < 0:
    number = int(input("Enter Number: "))
# dividir nro por cada numero desde 2 en adelante hasta llegar al numero. 
# si el resto da 0 en alguna operacion, entonces el nro no es primo
counter = 2
isPrime = True
while counter < number:
    if number % counter == 0: # si es divisible por algun numbero en la iteracion, entonces no es primo
        print(f"{number} is not PRIME")
        isPrime = False
        break
    counter += 1
if isPrime: # si el contador alcanzó al numero y ningun nro del contador logro dar resto 0 dividiendo al nro
    print(f"{number} is PRIME")