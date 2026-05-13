# Mensajes informativos del programa
print("Bienvenido a tu programa calculador de (IMC)")
print("Fórmula: IMC = peso / (altura2)")
print("por favor digita la siguiente informacion para calcular el IMC")
# peso de el usuario ingresarlo en una variable y transofrmado a float
peso=float(input("Digita tu peso en Kg: "))
# Altura debe ingresarse en decimal.
altura=float(input("Digita tu altura en metros: ")) 
indice_masa_corporal = peso/(altura**2)

# Condicional
if indice_masa_corporal < 18.5:
    print("Bajo peso") 
elif indice_masa_corporal >= 18.5 and indice_masa_corporal <= 24.9:
    print("Peso normal")
elif indice_masa_corporal >= 25 and indice_masa_corporal <= 29.9:
    print("Sobrepeso")
elif indice_masa_corporal >= 30:
    print("Obesidad")

print("Gracias por usar nuestro modulo de IMC")





