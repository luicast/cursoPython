from typing import Text


def run():
    # for contador in range(100):
    #     if contador % 2 != 0:
    #      continue
    #     print(contador)
    
    # for i in range(100):
    #     print(i)
    #     if i == 56:
    #         break
    
    Texto =  input("escribe un texto: ")
    for letter in Texto:
        if letter == "o":
            break
        print(letter)


if __name__ == "__main__":
    run()
