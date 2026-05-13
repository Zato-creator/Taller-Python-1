def area_cuadrado (lado):
    area_cuadrado_resultado = lado ** 2
    return area_cuadrado_resultado 

def area_rectangulo (base, altura):
    area_rectangulo_resultado = base * altura
    return area_rectangulo_resultado

def area_triangulo (base, altura):
    area_triangulo_resultado = (base*altura)/2
    return area_triangulo_resultado

def area_circulo (radio):
    area_circulo_resultado = 3.14159 * (radio**2)
    return area_circulo_resultado

print("=================================================")
print("Bienvenido a tu programa calculadora de areas")
print("=================================================")

print("Menú ")
print("Digita la opcion de la figura la cual desees hallar el area:")
print("1. Hallar el area del cuadrado\n2. Hallar el area del rectangulo\n3. Hallar el area de el triangulo\n4. Hallar el area del circulo\n5. salir")
opcion = input("Digite la opcion del area que desa hallar: ")

if opcion == 1:
    