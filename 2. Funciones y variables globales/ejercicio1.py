import os

def area_cuadrado():
    lado = float(input("Ingresa el lado del cuadrado en cm: "))
    resultado = lado ** 2
    return resultado

def area_rectangulo():
    base = float(input("Ingresa la base de tu rectangulo en cm: "))
    altura = float(input("Ingresa la altura de tu rectangulo en cm: "))
    resultado = base * altura
    return resultado

def area_triangulo():
    base = float(input("Ingresa la base de tu triangulo en cm: "))
    altura = float(input("Ingresa la altura de tu triangulo en cm: "))
    resultado = (base * altura) / 2
    return resultado

def area_circulo():
    radio = float(input("Ingresa el radio de tu circulo: "))
    resultado = 3.14159 * (radio ** 2)
    return resultado

print("=================================================")
print("Bienvenido a tu programa calculadora de areas")
print("=================================================")

while True:
    os.system("cls")
    print("Menú ")
    print("Digita la opcion de la figura la cual desees hallar el area:")
    print("1. Hallar el area del cuadrado\n2. Hallar el area del rectangulo\n3. Hallar el area de el triangulo\n4. Hallar el area del circulo\n5. salir")
    opcion = int(input("Digite la opcion del area que desa hallar: "))
    if opcion == 1:
        res = area_cuadrado() 
        print(f"El área del cuadrado es: {res}")
        os.system("pause")

    elif opcion == 2:
        res = area_rectangulo()
        print(f"El área del rectángulo es: {res}")
        os.system("pause")

    elif opcion == 3:
        res = area_triangulo()
        print(f"El área del triángulo es: {res}")
        os.system("pause")

    elif opcion == 4:
        res = area_circulo()
        print(f"El área del círculo es: {res}")
        os.system("pause")

    elif opcion == 5:
        print("Gracias por usar nuestros servicios, ¡feliz día!")
        break