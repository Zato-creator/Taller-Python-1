print("Bienvenido a tu programa colntador de numeros pares ")
print("====================================================")

numero = 0
while numero < 1:
    try:
        numero = float(input("Ingresa un numero mayor a zero: "))
        
        if numero < 1:
            print("Error: El numero debe ser mayor a 0.")
            
    except ValueError:
        print("¡Error! Por favor, ingresa solo números (sin letras).")
        numero = 0
i = 0
contador_par = 0
for i in  range(1, int(numero) +1):
    numero_par = i % 2
    if numero_par == 0:
        contador_par = contador_par +1

print(f"De la cantidad de numeros que deseaste revisar {numero} encontramos que hay {contador_par} numeros pares")
print("==================================================================================================")
print("Gracias por utilizar nuestro software feliz resto de día")
