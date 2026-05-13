print("Bienvenido a su programa de calculador de edad")
print("==============================================")
edad = 0
while edad < 1:
    try:
        edad = int(input("Ingresa tu edad: "))
        
        if edad < 1:
            print("Error: La edad debe ser mayor a 0.")
            
    except ValueError:
        print("¡Error! Por favor, ingresa solo números (sin letras).")
        edad = 0

if edad >= 0 and edad <= 12:
    print(f"Tienes {edad} eres un niño")
elif edad >= 13 and edad <= 17:
    print(f"Tienes {edad} eres un adolecente")
elif edad >= 18 and edad <= 64:
    print(f"Tienes {edad} eres un adulto")
elif edad > 65:
    print(f"Tienes {edad} eres un adulto mayor")