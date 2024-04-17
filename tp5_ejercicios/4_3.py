ventasTotal = 0
ventasDescuento_10 = 0
ventasDescuento_20 = 0
ventasPrecioBase = 0
cantidadProducto = 0
precioBase = int(input("Ingresar precio base: "))
while cantidadProducto != -1:
    cantidadProducto = int(input("Ingresar cantidad del producto: "))
    if cantidadProducto < 13 and cantidadProducto > 0:
        ventasPrecioBase += cantidadProducto
        print(f"Valor de la venta es: {cantidadProducto * precioBase}")
    elif cantidadProducto > 12 and cantidadProducto < 101:
        ventasDescuento_10 += cantidadProducto
        print(f"Valor de la venta es: {(precioBase - (10 * precioBase / 100)) * cantidadProducto}")
    elif cantidadProducto > 99:
        ventasDescuento_20 += cantidadProducto
        print(f"Valor de la venta es: {(precioBase - (20 * precioBase / 100)) * cantidadProducto}")
ventasTotal = ventasPrecioBase + ventasDescuento_10 + ventasDescuento_20
print(f"Ventas total: {ventasTotal}\nVentas a precio base: {ventasPrecioBase}\nVentas con 10% de descuento: {ventasDescuento_10}\nVentas con 20% de descuento: {ventasDescuento_20}")


        
        

