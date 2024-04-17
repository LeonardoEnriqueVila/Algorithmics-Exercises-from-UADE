# Costo basico del libro: 5000
# 32 por pagina
# si el nro de paginas supera las 300 -> costo +1200
# si paginas es 600+ -> +3360

price = 5000
numOfPages = int(input("Enter number of book pages: "))
price += numOfPages * 32
if numOfPages > 300:
    price += 1200
if numOfPages > 600:
    price += 3360

print(f"Price is ${price} for a book with {numOfPages} pages")

