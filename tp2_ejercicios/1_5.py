medicationPrice = int(input("Enter medication price: "))
newPrice = medicationPrice
newPrice -= 35 * medicationPrice / 100
print(f"Original price: {medicationPrice}\nPrice after discount: {newPrice}\nDiscount amount: {medicationPrice - newPrice}")