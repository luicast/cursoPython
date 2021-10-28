def palindromo(palabra):
    palabra = palabra.replace(" ","")
    palabra = palabra.lower()
    palabraInvertida = palabra[::-1]
    if palabra == palabraInvertida:
        return True
    else:
        False


def run():
    palabra = input(" escribe una palabra: ")
    esPalindromo = palindromo(palabra)
    if esPalindromo == True:
        print("es palindromo")
    else:
        print("no es palindromo")


if __name__ == "__main__":
    run()