print("Bienvenido a tu tienda virtual D-one")
print("================================================")
nombre_producto = input("ingresa el nombre del producto: ")
precio_por_unidad = float(input("Ingresa el precio por unidad del producto nombrado: "))
cantidad_comprar = float(input("cantidad a comprar: "))
subtotal = cantidad_comprar*precio_por_unidad
valor_iva = subtotal * (19/100)
total_pagar = subtotal + valor_iva
print(f"Tu compra tiene un valor de: {total_pagar} con un IVA {valor_iva} ")
print("====================================================================")
print("Gracias por usar nuestro sistema de registro de ventas ¡HASTA LA PROXIMA!")
