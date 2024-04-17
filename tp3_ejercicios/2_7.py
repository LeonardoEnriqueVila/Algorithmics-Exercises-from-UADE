# viaje minimo 2700
# entre 0 y 10 km -> 400 por km
# 10km o mas -> 200 por km
price = 0
km = int(input("Enter number of kilometers: "))
if km < 10:
    price = km * 400
elif km > 9:
    price = km * 200
if price < 2700:
    price = 2700

print(f"Price for {km}km is: {price}")