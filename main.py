import random

# 2) 
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
  print("Dispone de $", pozo)
  pozo += solicitar_fondos()
  return pozo

def solicitar_fondos():
  monto = int(input("Ingrese monto para el pozo (entre 5 y 100000): $"))

  while monto < 5 or monto > 100000:
    print("❌ ERROR! ❌ La cantidad ingresada no es valida (Mínimo 5 - Máximo 100000)")
    monto = int(input("Ingrese monto para el pozo (entre 5 y 100000): $"))

  return monto

def solicitar_apuesta():
  pass

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

def jugar_mano():
  carta_jugador_1 = generar_carta()
  carta_jugador_2 = generar_carta()
  puntaje_jugador = obtener_puntaje_carta(carta_jugador_1, 0)
  puntaje_jugador += obtener_puntaje_carta(carta_jugador_2, puntaje_jugador)
  es_bj_nat_jug = es_blackjack(puntaje_jugador)
  
  carta_crupier_1  = generar_carta()
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
  while puntaje_jugador <= 21 and (robo is None or len(robo) == 0 or robo not in ("s", "n") or robo == 's'):
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

  es_bj_nat_crup = False
  es_seg_carta_crupier = True
  
  print("\n>> Juego Crupier")
  while puntaje_crupier <= 16:
    print(">> El crupier da otra carta...")
    nueva_carta = generar_carta()
    puntaje_crupier += obtener_puntaje_carta(nueva_carta, puntaje_crupier)
    str_cartas_crupier += mostrar_carta(nueva_carta)
    print(str_cartas_crupier)
    print(">> Puntaje actual:", puntaje_crupier)

    # Comprobar si el crupier tiene un bj natural en la 2da carta
    if es_seg_carta_crupier:
      if puntaje_crupier == 21:
        es_bj_nat_crup = True
        
      es_seg_carta_crupier = False
    
# -1 Gana el crupier
# 0  Empate
# 1  Gana el jugador
def definir_ganador(puntaje_jugador, puntaje_crupier):
  #if puntaje_jugador == puntaje_crupier:
  #  print('empate')
  #elif puntaje_
  #elif puntaje_jugador > puntaje_crupier:
  pass
  

def generar_carta():
  cartas = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
  palos = ("♥", "♦", "♣", "♠")

  valor_carta = random.randint(1, 13) # Es representación de la carta ENTERO
  carta = cartas[valor_carta - 1] # Signo de la carta STRING
  palo = random.choice(palos) # Palo de la carta STRING

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

while opc is None or opc != 3:
  opc_str = input(menu)
  if es_valido(opc_str):
    opc = int(opc_str) # Convertirlo en Int solo cuando el STR es valido
    if opc == 1:
      monto = agregar_al_pozo(monto)
    elif opc == 2:
      jugar_mano()
  else:
    print("❌ ERROR! ❌: seleccione una opción entre 1  y 3")
    