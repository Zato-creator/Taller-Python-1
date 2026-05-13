print("Bienvenidos a su sistema de conversion de tiempo de minutos a horas y minutos.")
print("==================================================================")

minutos = float(input("Ingresa la cantidad de minutos: "))
horas = minutos // 60 
minutos_restantes = minutos % 60
print(f"Tu convertidor informa que {minutos} es igual a {horas} horas y {minutos_restantes} minutos")
print("Gracias por utilizar nuestros servicios feliz dia.")