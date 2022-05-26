import random

# 2) realizar una apuesta, multiplo de 5 y menor al pozo
"""
El jugador recibe dos cartas inicialmente y a partir de ese momento puede seguir pidiendo cartas hasta que decida frenar o bien logre 21 o se pase.
El valor del AS no es fijo. Cuando el jugador o el crupier lo recibe puede sumar 11 mientras no pase de 21. Si siguiera pidiendo cartas y se pasara, el valor del AS vuelve a 1.
El crupier inicialmente recibe una carta que se muestra junto con las dos primeras cartas del jugador. Su juego continúa cuando el jugador termina. Debe pedir cartas mientras tenga 16 o menos de puntaje y plantarse con 17 o más, siendo indefinida la cantidad de cartas hasta lograrlo.
El blackjack natural le gana a un blackjack conseguido con 3 cartas o más.
El ganador de la partida es quien logra 21 o el valor más próximo sin pasarse. Las posibles opciones son:
Gana el jugador: Recibe el doble de su apuesta. (si tenía 10 y apostó 5, queda con 15).
Pierde el jugador: En esta ocasión no pueden perder ambos. Si el jugador pierde y el crupier también, gana el crupier. (si tenía 10 y apostó 5, queda con 5).
Empatan: Si tanto el jugador como el crupier obtienen el mismo puntaje (21 o menos) entonces el jugador recibe su apuesta. (si tenía 10 y apostó 5, queda con 10).
En cada mano se debe mostrar:
Monto inicial del pozo (previo a la apuesta).
Monto de la apuesta.
Cartas de cada jugador y su puntaje final.
Mensaje indicando quién es el ganador.
Monto actualizado del pozo.
"""

# 3) Salir

"""
Salir: Cuando el usuario elige esta opción se debe mostrar su pozo actualizado y los siguientes resultados:

El porcentaje de victorias del jugador.
La racha más larga de victorias del croupier.
La cantidad de manos donde hubo un blackjack natural
El monto máximo que llegó a tener el jugador en el pozo.
El monto promedio del que dispuso el jugador para realizar apuestas.
La pérdida más grande que sufrió el jugador (si hubo alguna)"""


def es_valido(num):
    numeros = ("1", "2", "3")
    return num in numeros

  
def agregar_al_pozo(pozo):
    print("Dispone de $", pozo, sep="")
    pozo += solicitar_fondos()
    return pozo


def solicitar_fondos():
    fondos = int(input("Ingrese monto para el pozo (entre 5 y 100000): $"))

    while fondos < 5 or fondos > 100000:
        print("❌ ERROR! ❌ La cantidad ingresada no es valida (Mínimo 5 - Máximo 100000)")
        fondos = int(input("Ingrese monto para el pozo (entre 5 y 100000): $"))

    return fondos


def generar_carta():
    cartas = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    palos = ("♥", "♦", "♣", "♠")

    # valor_carta = random.randint(1, 13)  # Es representación de la carta ENTERO
    # carta = cartas[valor_carta - 1]  # Signo de la carta STRING
    carta = random.choice(cartas)  # Valor carta STRING
    palo = random.choice(palos)  # Palo de la carta STRING

    # TUPLA: (VALOR CARTA, CARTA, PALO)
    return carta, palo


def puntaje_carta(c1, *c2):
    if c1[0] == "J" or c1[0] == "Q" or c1[0] == "K":
        valor_1 = 10
    elif c1[0] == "A":
        valor_1 = 11
    else:
        valor_1 = int(c1[0])

    puntaje_parcial = valor_1
    if len(c2) != 0:
        for c in c2:
            if c[0] == "J" or c[0] == "Q" or c[0] == "K":
                valor_2 = 10
            elif c[0] == "A":
                valor_2 = 11
            else:
                valor_2 = int(c[0])
            if c1[0] == "A" and c[0] == "A":
                valor_2 = 1

            puntaje_parcial += valor_2

            if puntaje_parcial > 21 and (c1[0] == "A" or c[0] == "A"):
                puntaje_parcial -= 10

    return puntaje_parcial


def apuestas(pozo):
    apuesta = int(input("Realice su apuesta (Debe ser un multiplo de 5):_$"))
    while apuesta > pozo:
        apuesta = int(input("ERROR! La apuesta no puede ser mayor al pozo! Realice su apuesta:_$"))
    while apuesta < 1:
        apuesta = int(input("ERROR! La apuesta no puede ser menor a $1! Realice su apuesta:_$"))
    while apuesta % 5 != 0:
        apuesta = int(input("ERROR! La apuesta debe ser un múltiplo de 5! Realice su apuesta:_$"))
    return apuesta


def fin_mano():
    fin_mano_1 = """
    1- Pedir otra carta
    2- Plantarse
    """
    eleccion = None
    while eleccion is None or eleccion != 2:
        eleccion = input(fin_mano_1)
        if es_valido(eleccion):
            eleccion = int(eleccion)
            if eleccion == 1:
                carta = generar_carta()
                return carta
        else:
            print("❌ ERROR! ❌: seleccione una opción entre 1 y 2")


def determinar_ganador(puntos_pj, puntos_pc, bj_nat_pj=False, bj_nat_pc=False):
    print("Puntos croupier:", puntos_pc)
    print("Puntos", jugador, puntos_pj)
    if puntos_pj == 21:
        print("BlackJack! para", jugador)
    if puntos_pc == 21:
        print("BlackJack! para croupier")
    if puntos_pj > 21:
        print(jugador, "se paso de 21!")
    if puntos_pc > 21:
        print("El croupier se paso de 21!")
    if 21 >= puntos_pj > puntos_pc or puntos_pc > 21 and puntos_pj <= 21:
        print("Gana ", jugador, "!", sep="")
        ganador = 1
        return ganador
    if 21 >= puntos_pc > puntos_pj or puntos_pj > 21 and puntos_pc <= 21:
        print("Gana croupier!")
        ganador = 2
        return ganador
    if (puntos_pc == puntos_pj and puntos_pj <= 21) or (bj_nat_pj and bj_nat_pc):
        print("Es un empate!")
        ganador = 0
        return ganador
    if puntos_pj > 21 and puntos_pc > 21:
        print("Ambos se pasaron de 21, gana croupier!")
        ganador = 2
        return ganador
    if bj_nat_pc and puntos_pj == 21:
        print("Gana croupier por BlackJack natural!")
        ganador = 2
        return ganador
    if bj_nat_pj and puntos_pc == 21:
        print("Gana", jugador, "por BlackJack natural!")
        ganador = 1
        return ganador


def fin_ronda(gano, pozo, ficha):
    global gano_pj, gano_pc, gano_pj, racha_pc, racha_pj, cant_manos
    cant_manos += 1
    #  FALTA GUARDAR LA MEJOR RACHA
    if gano == 1:
        gano_pj += 1
        racha_pj += 1
        racha_pc = 0
        pozo += ficha
        return pozo
    elif gano == 2:
        gano_pc += 1
        racha_pc += 1
        racha_pj = 0
        pozo -= ficha
        return pozo
    elif gano == 0:
        racha_pc = 0
        racha_pj = 0
        return pozo


def jugar_mano(fondos):
    global bj_nat
    bj_nat_pj = bj_nat_pc = False
    print("Dispone de $", fondos, sep="")
    if fondos < 5:
        print("No tenés fondos suficientes para apostar!")
        fondos = agregar_al_pozo(fondos)
    ficha = apuestas(fondos)
    print("\nApostaste: $", ficha, sep="")

    #  Mano 1
    carta_pc_1 = generar_carta()  # Genera 1 carta para el croupier
    print("\nCartas croupier:\n", carta_pc_1)
    puntaje_parcial_pc = puntaje_carta(carta_pc_1)
    print("Puntaje parcial croupier:", puntaje_parcial_pc)  # Muestra puntaje parcial croupier
    carta_pj_1 = generar_carta()
    carta_pj_2 = generar_carta()  # Genera 2 cartas para el jugador
    print("\nCartas", jugador, ":\n", carta_pj_1, carta_pj_2)
    puntaje_parcial_pj = puntaje_carta(carta_pj_1, carta_pj_2)
    print("Puntaje parcial", jugador, ":", puntaje_parcial_pj)  # Muestra puntaje parcial del jugador

    #  Mano 2 jugador
    if puntaje_parcial_pj == 21:
        print("BlackJack natural", jugador, "!")
        bj_nat_pj = True
        bj_nat += 1
    if puntaje_parcial_pj < 21:
        carta_pj_3 = fin_mano()
        if carta_pj_3:
            print("\nCartas", jugador, ":\n", carta_pj_1, carta_pj_2, carta_pj_3)
            puntaje_parcial_pj = puntaje_carta(carta_pj_1, carta_pj_2, carta_pj_3)
            print("Puntaje parcial", jugador, ":", puntaje_parcial_pj)
        if carta_pj_3 and puntaje_parcial_pj < 21:
            carta_pj_4 = fin_mano()
            if carta_pj_4:
                print("\nCartas", jugador, ":\n", carta_pj_1, carta_pj_2, carta_pj_3, carta_pj_4)
                puntaje_parcial_pj = puntaje_carta(carta_pj_1, carta_pj_2, carta_pj_3, carta_pj_4)
                print("Puntaje parcial", jugador, ":", puntaje_parcial_pj)

    #  Jugada pc
    if puntaje_parcial_pc < 16:
        carta_pc_2 = generar_carta()
        print("\nCartas croupier:\n", carta_pc_1, carta_pc_2)
        puntaje_parcial_pc = puntaje_carta(carta_pc_1, carta_pc_2)
        print("Puntaje parcial croupier:", puntaje_parcial_pc)
        if puntaje_parcial_pc == 21:
            print("BlackJack natural croupier!")
            bj_nat += 1
            bj_nat_pc = True
        if puntaje_parcial_pc < 16:
            carta_pc_3 = generar_carta()
            print("\nCartas croupier:\n", carta_pc_1, carta_pc_2, carta_pc_3)
            puntaje_parcial_pc = puntaje_carta(carta_pc_1, carta_pc_2, carta_pc_3)
            print("Puntaje parcial croupier:", puntaje_parcial_pc)
            if carta_pc_3 and puntaje_parcial_pc < 16:
                carta_pc_4 = generar_carta()
                print("\nCartas croupier:\n", carta_pc_1, carta_pc_2, carta_pc_3, carta_pc_4)
                puntaje_parcial_pc = puntaje_carta(carta_pc_1, carta_pc_2, carta_pc_3, carta_pc_4)
                print("Puntaje parcial croupier:", puntaje_parcial_pc)

    print()
    ganador = determinar_ganador(puntaje_parcial_pj, puntaje_parcial_pc, bj_nat_pj, bj_nat_pc)
    fondos = fin_ronda(ganador, monto, ficha)
    return fondos


# INICIO
#  Variables iniciadas
gano_pj = gano_pc = racha_pc = racha_pj = cant_manos = bj_nat = 0
pozo_max = monto_total = perdida_max = 0

# Nombre del jugador
jugador = input("Ingrese nombre del jugador: ")
if len(jugador) == 0:
    print("El jugador se quiere mantener en el anonimato, se lo llamara: Anónimo")
    jugador = "Anónimo"
print("Bienvenido,", jugador)

# Monto para el pozo
monto = solicitar_fondos()
pozo_max = monto
monto_total = monto

# Ejecutar el menu
menu = """
Menu:
  1- Apostar
  2- Jugar una mano
  3- Salir

Ingrese una opción:"""

opc = None
while opc is None or opc != 3:
    opc_str = input(menu)
    if es_valido(opc_str):
        opc = int(opc_str)  # Convertirlo en Int solo cuando el STR es valido
        if opc == 1:
            print("APOSTAR:\n")
            monto = agregar_al_pozo(monto)
            monto_total += monto
            if monto > pozo_max:
                pozo_max = monto
        elif opc == 2:
            print("JUGAR UNA MANO:\n")
            monto = jugar_mano(monto)
            monto_total += monto
            if monto > pozo_max:
                pozo_max = monto
            print("Tu pozo es de: $", monto)
    else:
        print("❌ ERROR! ❌: seleccione una opción entre 1 y 3")

# Datos de salida
print("SALIR")
if cant_manos > 0:
    porc_victorias = (gano_pj * 100) / cant_manos
    print("El porcentaje de victorias de ", jugador, ": %", round(porc_victorias, 2), sep="")
    prom_monto = monto_total / cant_manos
    print("El monto promedio del que dispuso ", jugador, " para realizar apuestas: $", prom_monto, sep="")
print("La racha más larga de victorias del croupier:", racha_pc)
print("La cantidad de manos donde hubo un blackjack natural:", bj_nat)
print("El monto máximo que llegó a tener ", jugador, " en el pozo: $", pozo_max, sep="")
