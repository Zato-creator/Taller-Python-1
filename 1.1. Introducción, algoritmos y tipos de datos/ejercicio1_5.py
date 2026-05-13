print("Calculador de la propina de un restaurante")
print("============================================================")
cuenta = 0
propina = 0
while cuenta < 1 or propina < 1:   
    cuenta = float(input("Ingresa le valor de la cuenta: "))
    propina = float(input("Ingresa el porsentage de propina que desas dejar 10, 15 o 20 porciento: "))

calculo_propina = cuenta * (propina/100)
total_pagar = cuenta + calculo_propina

print("============================================================")
print(f"El valor de la cuenta es de: {cuenta} pesos")
print(f"El valor de la propina de {propina}% es de {calculo_propina} pesos")
print(f"El total a pagar con servicio es de {total_pagar} pesos")
print("============================================================")
print("Gracias por usar nuestro software")
