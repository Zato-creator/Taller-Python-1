import random

numero_secreto = 0
intentos = 0
ganado = False

def generar_numero():
    global numero_secreto, intentos, ganado
    numero_secreto = random.randint(1, 100)
    intentos = 0
    ganado = False

def registrar_intento():
    global intentos
    intentos += 1

def verificar_adivinanza(usuario_num):
    global ganado
    registrar_intento()
    
    if usuario_num < numero_secreto:
        print("Mas alto...")
        return False
    elif usuario_num > numero_secreto:
        print(" Mas bajo...")
        return False
    else:
        print(" ¡Exacto! Has acertado.")
        ganado = True
        return True

def mostrar_estadisticas():
    print("\n--- ESTADÍSTICAS FINALES ---")
    print(f"Número secreto: {numero_secreto}")
    print(f"Total de intentos: {intentos}")
    if intentos <= 5:
        print("Calificación: ¡Eres un genio!")
    elif intentos <= 10:
        print("Calificación: ¡Nada mal!")
    else:
        print("Calificación: Puedes mejorar, ¡sigue practicando!")
    print("----------------------------\n")

def jugar():
    generar_numero()
    print("¡Bienvenido al juego de adivinanza!")
    print("He pensado un número entre 1 y 100. ¿Puedes adivinarlo?")

    while not ganado:
        try:
            entrada = int(input("Introduce tu número: "))
            verificar_adivinanza(entrada)
        except ValueError:
            print("Por favor, introduce un número válido.")

    mostrar_estadisticas()

if __name__ == "__main__":
    jugar()
