import os

notas_globales = []

def agregar_nota():
    nueva_nota = float(input("Digita la nota que deseas agregar: "))
    notas_globales.append(nueva_nota)
    print(f"Nota {nueva_nota} agregada correctamente.")

def calcular_promedio():
    if not notas_globales:
        return 0
    return sum(notas_globales) / len(notas_globales)

def contar_notas():
    return len(notas_globales)

def reset_notas():
    notas_globales.clear()
    print("Sistema reiniciado. Todas las notas han sido eliminadas.")

while True:
    os.system("cls") 
    print("========================================================")
    print("Bienvenido a tu programa al sistema de notas estudiantil")
    print("========================================================")
    print("Menú ")
    print("1. Agregar nota\n2. Calcular promedio\n3. Cuente las notas\n4. Restablecer notas\n5. Salir")
    
    
    try:
        opcion = int(input("Digite la opcion deseada: "))
        
        if opcion == 1:
            agregar_nota() 
            os.system("pause")

        elif opcion == 2:
            res = calcular_promedio()
            print(f"El promedio de las notas es: {res:.2f}")
            os.system("pause")

        elif opcion == 3:
            res = contar_notas()
            print(f"La cantidad de notas es de: {res}")
            os.system("pause")

        elif opcion == 4:
            reset_notas()
            os.system("pause")

        elif opcion == 5:
            print("Gracias por usar nuestros servicios, ¡feliz día!")
            break
        else:
            print("Opción no válida.")
            os.system("pause")
            
    except ValueError:
        print("Por favor, introduce un número válido.")
        os.system("pause")

print("\nRESUMEN DEL SISTEMA ---")
print(f"Total de notas: {contar_notas()}")
print(f"Promedio actual: {calcular_promedio():.2f}")
print(f"Lista de notas: {notas_globales}")
print("=======================================================")