from convertidorMonedaMejorado import mensaje


def run():
    nombre = input("escribe tu nombre: ")
    cont = 0
    for letter in nombre:
        print(letter)
        if letter == " ":
            cont = cont
        else:
            cont += 1
    print("tu nombre tiene " + str(cont) + " letras" )
    mensaje()


def mensaje():
    msj = input("desea realizar de nuevo [y/n]: ")
    if msj == "y":
        run()
    else:
        print("adios")


if __name__ == "__main__":
    run()