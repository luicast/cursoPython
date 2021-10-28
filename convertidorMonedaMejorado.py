def conversor(tipoPesos, valorDolar):
    pesos = input("cuantos pesos " + tipoPesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valorDolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")


def mensaje():
    msj = input("desea realizar otra conversion [y/n]: ")
    if msj == "y":
        elMenu()
    else:
        print("gracias por usar este servicio")


def elMenu():
    menu = """
    Bienvenido al conversor de moneda💰

    1- pesos colombianos
    2- pesos argentinos
    3- pesos mexicanos
    4- salir

    eligie una opcion: """

    opcion = int(input( menu))

    if opcion == 1:
        conversor("colombianos", 3875)
        mensaje()
    elif opcion == 2:
        conversor("argentinos", 65)
        mensaje()
    elif opcion == 3:
        conversor("mexicanos", 24)
        mensaje()
    elif opcion == 4:
        input("gracias por usar este servicio")
    else:
        input("ingresa una opcion correcta!")
        elMenu()


if __name__ == "__main__":
    elMenu()