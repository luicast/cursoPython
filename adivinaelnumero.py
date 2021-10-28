import random

def  run():
    numeroAleatorio = random.randint(1, 100)
    numeroElegido = int(input("elige un numero del 1 a 100: "))
    while numeroElegido != numeroAleatorio:
        if numeroElegido < numeroAleatorio:
            print("busca un numero mas grande")       
        else:
            print("busca un numero mas pequeno")
        numeroElegido = int(input("elige otro numero: "))
    print("ganaste!")


if __name__ == "__main__":
    run()