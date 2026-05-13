print("Bienvenido a su software de manipulacion de texto \n"
      "================================================= " )
frase = input("ingresa la frase a manipular: ")
palabra = frase.split()
print(f"Esta es la frase en mayuscula: {frase.upper()}")
print(f"Esta es la frase en minuscula: {frase.lower()}")
print(f"Esta es la cantidad de palabras en la frase {len(palabra)}")
print(f"Esta es la primera palabra de la frase: {palabra[0]}")
print(f"Esta es ka ultima palabra de la frase: {palabra[-1]}")

print("=================================================")
print("Gracias por usar nuestro software, hasta protno")

