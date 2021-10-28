menu = """
Bienvenido al conversor de moneda💰

1- pesos colombianos
2- pesos argentinos
3- pesos mexicanos

eligie una opcion: """

opcion = int(input( menu))

if opcion == 1:
    pesos = input("cuantos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valorDolar = 3875
    dolares = pesos / valorDolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")
elif opcion == 2:
    pesos = input("cuantos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valorDolar = 65
    dolares = pesos / valorDolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")
elif opcion == 3:
    pesos = input("cuantos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    valorDolar = 24
    dolares = pesos / valorDolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")
else:
    input("ingresa una opcion correcta!")
