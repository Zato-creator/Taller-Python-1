print("=============================================================")
print("Bienvenido a tu programa de validador de cntraseña")
print("=============================================================")

contrasena = input("Digita la contraseña esta debe ser alfanumerica \nes decir puede contener simbolos, letras y numeros")

contador_intentos = 0

while contrasena != "python123":
    print("La contraseña no es correcta acceso denegado, intentalo de nuevo")
    contador_intentos = contador_intentos + 1

    contrasena = input("Intentalo de nuevo: ") 

print("=============================================================")
print(f"Acceso concedido la cantidad de intentos fue de {contador_intentos} intentos")