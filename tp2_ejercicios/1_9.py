# Generar una cantidad random de vendedores (desde 1 a 20)
# Crear un diccionario dinamico en el que se guarda key: vendedor - value: lista con valores de vendedor
# generar valores de vendedor de forma aleatoria tambien
    # salarioBasico, cantidad de ventas, comision por cantidad de ventas, comision del 5% del valor de las ventas y el salario final
# el programa pide solicitar informacion de x nro de vendedores (segun los que se generaron)
# Luego imprime los valores ya calculados y asignados en el generador 
import random
def generateSellAmount(sells, minValue, maxValue): 
    sellSum = 0
    for _ in range(0, sells):
        sellSum += random.randint(minValue, maxValue)
    return sellSum

def switchRanks(rank, sellerData): 
    match rank:
        case "Noob":
            sellerSells = random.randint(1, 5)
            sellVolume = generateSellAmount(sellerSells, 100000, 250000)
            commissionQuantity = 50000 * sellerSells
            commissionVolume = 5 * sellVolume / 100
            salary = 250000 + commissionQuantity + commissionVolume
        case "Intermediate":
            sellerSells = random.randint(4, 20)
            sellVolume = generateSellAmount(sellerSells, 100000, 550000)
            commissionQuantity = 50000 * sellerSells
            commissionVolume = 5 * sellVolume / 100
            salary = 250000 + commissionQuantity + commissionVolume
        case "Pro":
            sellerSells = random.randint(10, 20)
            sellVolume = generateSellAmount(sellerSells, 100000, 1000000)
            commissionQuantity = 50000 * sellerSells
            commissionVolume = 5 * sellVolume / 100
            salary = 250000 + commissionQuantity + commissionVolume
    sellerData.extend([sellerSells, sellVolume, commissionQuantity, commissionVolume, salary])

sellerRankList = ["Noob", "Intermediate", "Pro"]
numOfSellers = random.randint(1, 20)
sellersDict = {}

for seller in range(1, numOfSellers + 1):
    sellerRank = random.choice(sellerRankList)
    sellerData = [250000, sellerRank] # se inicializa con el salario basico y rango del seller
    switchRanks(sellerRank, sellerData)
    sellersDict[seller] = sellerData

while True: 
    sellerCall = int(input(f"{numOfSellers} aviable -> Enter seller ID: "))
    sellerStats = sellersDict[sellerCall]
    print(f"Seller {sellerCall} Stats: \nBasic Salary: {sellerStats[0]}\nRank: {sellerStats[1]}\nSells Amount: {sellerStats[2]}\nSells Volume: {sellerStats[3]}\nAmount Comission: {sellerStats[4]}\nVolume Comission: {sellerStats[5]}\nSalary: {sellerStats[6]}")


