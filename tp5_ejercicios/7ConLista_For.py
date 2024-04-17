# 1234 - numero
# 4321 - numero invertido
negativo = False
numero = (input("Ingresar dígitos: "))
if numero[0] == "-":
    numero = numero.replace("-", "")
    negativo = True
longitud = len(numero) 
numero_invertido = ""

for i in range(0, longitud):
    numero_invertido = numero[i] + numero_invertido
if negativo == False:
    print(numero_invertido)
else:
    print("-" + numero_invertido)




