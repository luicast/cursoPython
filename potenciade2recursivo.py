def run(num, rept):
    if num <= rept:
        cont = num
        print(str(2 ** cont) )
        run(num+1, rept)
    else:
        print("Fin!")


if __name__ == "__main__":
    repeticiones = int(input("Cuantas potencias de base 2: "))
    run(0, repeticiones)