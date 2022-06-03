def apuestas(pozo):
    apuesta = int(input("Realice su apuesta (Debe ser un multiplo de 5):_$"))
    while apuesta > pozo or apuesta < 1 or apuesta % 5 != 0:
        apuesta = int(input("ERROR! La apuesta no es valida. $"))
    print("SU APUESTA ES:", apuesta)

    return apuesta

apuestas(100)