def esPrimo(numero):
    contador = 0
    for i in range(1,numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


def mensaje():
    msj = input("desea realizar de nuevo [y/n]: ")
    if msj == "y":
        run()
    else:
        print("adios")


def run():
    numero = int(input("escribre un numero: "))
    if esPrimo(numero):
        print(f"el numero {numero} es primo")
        mensaje()
    else:
        print(f"el numero {numero} no es primo")
        mensaje()


if __name__ == "__main__":
    run()