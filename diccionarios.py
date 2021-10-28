def run():
    miDiccionario = {
        "llave1":1,
        "llave2":2,
        "llave3":3,
    }
    # print(miDiccionario["llave1"])
    # print(miDiccionario["llave2"])
    # print(miDiccionario["llave3"])

    poblacionPaises = {
        "argentina":44938712,
        "brasil":210147125,
        "colombia":50372424,
    }
    
    # for pais in poblacionPaises.keys():
    #     print(pais)
    
    # for pais in poblacionPaises.values():
    #     print(pais)

    for pais, poblacion in poblacionPaises.items():
        print(f"{pais} tiene {poblacion} habitantes")

if __name__=="__main__":
    run()