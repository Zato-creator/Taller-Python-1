print("Bienvenido a tu programa de calculadora de descuentos")
print("=====================================================")

monto = 0
while monto < 1:
    try:
        monto = int(input("Ingresa el valor de tu compra: "))
        
        if monto < 1:
            print("Error: El monto debe ser mayor a 0.")
            
    except ValueError:
        print("¡Error! Por favor, ingresa solo números (sin letras).")
        monto = 0

if monto > 100000:
    valor_descuento = monto * (15/100)
    total_pagar = monto + valor_descuento
elif monto > 50000 and monto <= 100000:
    valor_descuento = monto * (10/100)
    total_pagar = monto + valor_descuento
elif monto > 20000 and monto <= 50000:
    valor_descuento = monto * (5/100)
    total_pagar = monto + valor_descuento
else:
    valor_descuento = 0
    total_pagar = monto

print("==============================================================")
print(f"tu compra fue de {monto} pesos y tienes un descuento de {valor_descuento}$ pesos \nEl total a pagar es de {total_pagar}$ pesos")
print("==============================================================")
print("Gracias por utilizar nuestros servicios excelente dia: ")
