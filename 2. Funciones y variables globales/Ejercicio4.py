import os

def metros_cm_km ():
    metros = float("Ingrese los metros a convertir en centimetros y kilometros")
    centimetros = metros * 100
    kilometros = metros/ 1000
    print(f"Los {metros} m equivalen a {centimetros} cm")
    print(f"Los {metros} m equivalen a {kilometros} km ")

def kilos_gramos_libras ():
    kilos = float(input("Ingrese los kilogramos a convertir en gramos y libras"))
    gramos = kilos * 1000
    libras = kilos * 2.2046
    print(f"Los {kilos} Kg equivalen a {gramos} gramos")
    print(f"Los {kilos} Kg equivalen a {libras} libras")

def hora_gramos_libras ():
    horas = float(input("Ingrese las horas a convertir en minutos y segundos: "))
    minutos = horas * 60
    segundos = horas * 3600
    print(f"Los {horas} horas equivalen a {minutos} minutos")
    print(f"Los {horas} horas equivalen a {segundos} segundos")

print("==================================================")
print("Bienvenido a tu progrmaa de conversion de unidades")
print("==================================================")

metros = 0
kilos = 0
horas = 0

while True:
    print("Digita la opcion que deseas convertir")
    print("Menú\n1. Metros a centimetros y kilometors\n2. Kilos a gramos y libras\n3. Horas a minutos y segundos\n4. Salir\n===========================================")
    opcion = int(input("Digite la opcion: "))
    if opcion == 1:
        metros_cm_km ()
        os.system("pause")
    elif opcion == 2:
        kilos_gramos_libras ()
        os.system("pause")
    elif opcion == 3:
        hora_gramos_libras ()
        os.system("pause")
    elif opcion == 4:
        print("Gracias por utilizar nuestros servicios feliz dia.")
        break
