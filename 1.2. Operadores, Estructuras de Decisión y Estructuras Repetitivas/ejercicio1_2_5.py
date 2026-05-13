print("=========================================================================")
print("Bienvendio al menú de opciones")
print ("1. Sumar 2 numeros")
print ("2. Restar 2 numeros")
print ("3. Multiplicar 2 numeros")
print ("4. Salir")
print("=========================================================================")

numero = 0
while numero < 1:
    try:
        numero = int(input("Ingresa la opcion a escoger: "))
        
        if numero < 1 or numero > 4:
            print("Error: El numero debe ser de los que se observan en el menú de opiones .")
            print("=========================================================================")
            print("Bienvendio al menú de opciones")
            print ("1. Sumar 2 numeros")
            print ("2. Restar 2 numeros")
            print ("3. Multiplicar 2 numeros")
            print ("4. Salir")
            print("=========================================================================")
                        
    except ValueError:
        print("¡Error! Por favor, ingresa solo números (sin letras).")
        numero = 0

if numero == 4:
    print("Gracias por usar nuestro software de menú de opciones hasta pronto")