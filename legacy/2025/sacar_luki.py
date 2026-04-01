from random import choice
palabras = (["sol", "luna", "río", "nube", "gato", "perro", "mar", "pez", "flor", "casa"])
palabra = choice(palabras)
letras = input("Escribi 1 letra para eliminar: ")

letras = letras.upper()


def quitar(palabraa, letras):
    resultado = ""
    for letra in palabraa:
        if letra not in letras:
            resultado += letra
    return resultado

print("palabra :", palabra)
print("poalabra sin las letras:", quitar(palabra, letras))