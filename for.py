def tabla(numero):
    print("la tabla del " + str(numero))
    for i in range(1,11):
        print(str(numero) + "x" + str(i) + "=" +str(i*numero))


def mensaje():
    msj = input("desea realizar otra tabla de multiplicar [y/n]: ")
    if msj == "y":
        run()
    else:
        print("gracias por usar este servicio")


def run():
    menu = """
    LAS TABLAS DE MULTIPLICAR
    selecciona la tabla que quieres ver:
    - tabla del 1
    - tabla del 2
    - tabla del 3
    - tabla del 4
    - tabla del 5
    - tabla del 6
    - tabla del 7
    - tabla del 8
    - tabla del 9
    
    elija una tabla: """
    
    opcion = str(input(menu))

    if opcion == "1":
        tabla(1)
        mensaje()
    elif opcion == "2":
        tabla(2)
        mensaje()
    elif opcion == "3":
        tabla(3)
        mensaje()
    elif opcion == "4":
        tabla(4)
        mensaje()
    elif opcion == "5":
        tabla(5)
        mensaje()
    elif opcion == "6":
        tabla(6)
        mensaje()
    elif opcion == "7":
        tabla(7)  
        mensaje() 
    elif opcion == "8":
        tabla(8)
        mensaje()
    elif opcion == "9":
        tabla(9)    
        mensaje()                     
    else:
        print('esa no es una opcion correcta')
        run()


if __name__ == "__main__":
    run()