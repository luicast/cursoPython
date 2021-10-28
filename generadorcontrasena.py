import random

def generarPassword(numero):
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    
    caracteres = MAYUS + MINUS + NUMS + CHARS
    contrasena = []

    for i in range(numero):
        caracterRandom = random.choice(caracteres)
        contrasena.append(caracterRandom)
    
    contrasena = "".join(contrasena)
    return contrasena


def mensaje():
    msj = input("desea realizar otra conversion [y/n]: ")
    if msj == "y":
        run()
    else:
        print("gracias por usar este servicio")


def run():
    cantidad = int(input("de cuantos caracteres deseas el nuevo password: "))
    contrasena = generarPassword(cantidad)
    print(f"tu nueva password es: {contrasena}")
    mensaje()

if __name__=="__main__":
    run()
