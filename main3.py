import random


def es_valido(num):  # Validar opciones del menú
    numeros = ("1", "2", "3")
    return num in numeros


def agregar_al_pozo(pozo):  # Agregar plata
    print("\nDispone de $", pozo)
    pozo += solicitar_fondos()
    return pozo


def restar_al_pozo(resta, pozo):  # new
    pozo -= resta
    return pozo


def def_apuesta(pozo):  # new
    print('Dispone de $', pozo)
    monto_apuesta = int(input('Ingrese la cantidad que quiere apostar (solo valores numericos que sean multiplos de 5):'))
    if pozo < 5:
        print('No dispone de suficiente dinero. Realize un deposito en el menu principal.')
        monto_apuesta = 0
    elif monto_apuesta > pozo:
        print('No dispone de suficiente dinero. Realize un deposito en el menu principal o reduzca su apuesta.')
        monto_apuesta = 0
    else:
        while monto_apuesta % 5 != 0:
            monto_apuesta = int(input('Su apuesta no es multiplo de 5. \nIngrese nuevamente su apuesta (solo valores numericos que sean multiplos de 5):'))

    return monto_apuesta


def solicitar_fondos():  # Solicitar dinero -new renombre var por pep8-
    ingreso = int(input("Ingrese monto para el pozo (entre 5 y 100000): $"))

    while ingreso < 5 or ingreso > 100000:
        print("❌ ERROR! ❌ La cantidad ingresada no es valida (Mínimo 5 - Máximo 100000)")
        ingreso = int(input("Ingrese monto para el pozo (entre 5 y 100000): $"))

    return ingreso


# Dada una carta y el puntaje actual, retorna el puntaje de la carta
def obtener_puntaje_carta(carta, puntaje_actual):
    if carta[0] >= 10:  # 10,J,Q,K
        return 10
    elif carta[0] == 1:  # A
        return obtener_valor_as(puntaje_actual)

    # Cualq otra
    return carta[0]


# Si el puntaje actual + 11 <= 21, entonces devolver 11
# Sino, devolver 1
def obtener_valor_as(puntaje_actual):
    if puntaje_actual + 11 <= 21:
        return 11

    return 1


def mostrar_carta(carta):
    return "[" + carta[1] + " " + carta[2] + "] "


def es_blackjack(puntaje):
    return puntaje == 21


def jugar_mano():  # -new def ganador- Juego
    # Definir primeras 2 cartas del jugador y posibilidad de bj nat
    carta_jugador_1 = generar_carta()
    carta_jugador_2 = generar_carta()
    puntaje_jugador = obtener_puntaje_carta(carta_jugador_1, 0)
    puntaje_jugador += obtener_puntaje_carta(carta_jugador_2, puntaje_jugador)
    bj_nat_jug = es_blackjack(puntaje_jugador)

    # Definir primer carta del crupier
    carta_crupier_1 = generar_carta()
    puntaje_crupier = obtener_puntaje_carta(carta_crupier_1, 0)
    str_cartas_jugador = mostrar_carta(carta_jugador_1) + mostrar_carta(carta_jugador_2)
    str_cartas_crupier = mostrar_carta(carta_crupier_1)

    print("\nMANO INICIAL")
    print(">> Cartas del jugador:")
    print(str_cartas_jugador)
    print(">> Puntaje actual:", puntaje_jugador)
    print("\n>> Cartas crupier:")
    print(str_cartas_crupier)
    print(">> Puntaje actual:", puntaje_crupier)

    robo = None

    # [] TO-DO: Refactor -> Agregar metodo
    while puntaje_jugador < 21 and (robo is None or len(robo) == 0 or robo not in ("s", "n") or robo == 's'):  # new sacar = o no termina while
        if robo is not None and robo != "s":
            print("Valor no valido")
        elif robo == "s":
            nueva_carta = generar_carta()
            puntaje_jugador += obtener_puntaje_carta(nueva_carta, puntaje_jugador)
            str_cartas_jugador += mostrar_carta(nueva_carta)
            print(str_cartas_jugador)
            print(">> Puntaje actual:", puntaje_jugador)

            if puntaje_jugador > 21:
                print(">> El jugador se pasó de 21.")

        if puntaje_jugador < 21:
            robo = input("\nQuiere robar otra carta (S/N)?:").lower()

    bj_nat_crup = False
    es_seg_carta_crupier = True

    print("\n>> Juego Crupier")
    while puntaje_crupier <= 16:
        print(">> El crupier roba otra carta...")  # new redaccion
        nueva_carta = generar_carta()
        puntaje_crupier += obtener_puntaje_carta(nueva_carta, puntaje_crupier)
        str_cartas_crupier += mostrar_carta(nueva_carta)
        print(str_cartas_crupier)
        print(">> Puntaje actual:", puntaje_crupier)

        # Comprobar bj nat del crupier
        if es_seg_carta_crupier:
            if puntaje_crupier == 21:
                bj_nat_crup = True

            es_seg_carta_crupier = False

    # Ganador de la mano
    ganador = definir_ganador(puntaje_jugador, puntaje_crupier, bj_nat_jug, bj_nat_crup)

    return ganador


def definir_ganador(puntaje_jugador, puntaje_crupier, bj_nat_jug, bj_nat_crup):  # new

    if puntaje_crupier > 21:
        puntaje_crupier = 0

    if puntaje_jugador > 21:
        puntaje_jugador = 0

    print('jug:', puntaje_jugador, 'crup:', puntaje_crupier)

    if bj_nat_crup and bj_nat_jug:
        mesa = 0
        bjnat = 2
    elif bj_nat_crup:
        mesa = -1
        bjnat = 1
    elif bj_nat_jug:
        mesa = 1
        bjnat = 1
    else:
        bjnat = 0
        if puntaje_crupier > puntaje_jugador:
            mesa = -1
        elif puntaje_crupier == 0 and puntaje_jugador == 0:
            mesa = -1
        elif puntaje_crupier == puntaje_jugador and puntaje_crupier != 0:
            mesa = 0
        else:
            mesa = 1

    return mesa, bjnat


def generar_carta():
    cartas = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
    palos = ("♥", "♦", "♣", "♠")

    valor_carta = random.randint(1, 13)  # Es representación de la carta ENTERO
    carta = cartas[valor_carta - 1]  # Signo de la carta STRING
    palo = random.choice(palos)  # Palo de la carta STRING

    # TUPLA: (VALOR CARTA, CARTA, PALO)
    return valor_carta, carta, palo


# ------ INICIO
# Nombre del jugador
jugador = input("Ingrese nombre del jugador: ")
# Si vacia se llama anonymus

if len(jugador) == 0:
    print("El jugador se quiere mantener en el anonimato, se lo llamara: Anónimo")
    jugador = "Anónimo"

print("Bienvenido,", jugador)

# Monto para el pozo
monto = solicitar_fondos()

menu = """
Menu:
  1- Apostar
  2- Jugar una mano
  3- Salir

Ingrese una opción:"""

opc = None
total_manos = gana_jug = gana_crup = cont_bjnat = pozo_max = acum_apuesta = perdida_max = racha = 0  # new

while opc is None or opc != 3:
    opc_str = input(menu)
    if es_valido(opc_str):
        opc = int(opc_str)  # Convertirlo en Int solo cuando el STR es valido
        if opc == 1:
            monto = agregar_al_pozo(monto)
        elif opc == 2:
            while pozo_max < monto:  # new Determinar el pozo maximo que obtuvo el jugador
                pozo_max = monto
            if monto > 5:
                apuesta = def_apuesta(monto)
                monto = restar_al_pozo(apuesta, monto)
                acum_apuesta += apuesta
                if apuesta != 0:
                    total_manos += 1
                    print('Bet: $', apuesta)
                    print('Pozo: $', monto)
                    final = jugar_mano()  # new revisar nombre var
                    if final[0] == 1:
                        gana_jug += 1
                        monto += (apuesta * 2)
                        cont_bjnat += final[1]
                        print('ganaste')
                        print('Dispone de $', monto)
                    elif final[0] == -1:
                        cont_bjnat += final[1]
                        gana_crup += 1
                        print('perdiste')
                        print('Dispone de $', monto)
                        if perdida_max < apuesta:
                            perdida_max = apuesta
                    else:
                        cont_bjnat += final[1]
                        monto += apuesta
                        print('Dispone de $', monto)
                        print('empayte')

            else:
                print('No dispone de suficiente dinero. Realize un deposito en el menu principal.')
    else:
        print("❌ ERROR! ❌: seleccione una opción entre 1 y 3")

porc_vic = (gana_jug * 100) // total_manos
promedio_apuesta = acum_apuesta / total_manos

print(jugador, 'ganó el %', porc_vic, 'de las manos jugadas.')
print('La racha mas larga de victorias del crupier fue de')
print('Hubo', cont_bjnat, 'Blackjacks naturales.')
print('El pozo maximo que el jugador obtuvo fue de: $', pozo_max)
print('El jugador aposto en promedio $', promedio_apuesta, 'por mano jugada.')
print('La perdida mas grande que sufrio el jugador fue de $', perdida_max)
