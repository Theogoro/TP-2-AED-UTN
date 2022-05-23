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


def puntaje_carta(c1, *c2=0):
  


def jugar_mano():
  carta_pc_1 = generar_carta() # Genera 1 carta para el croupier
  puntaje_parcial_pc = puntaje_carta(carta_pc_1) # Muestra puntaje parcial croupier
  carta_pj_1 = generar_carta() 
  carta_pj_2 = generar_carta() # Genera 2 cartas para el jugador
  puntaje_parcial_pj = puntaje_carta(carta_pj_1, carta_pj_2) # Muestra puntaje parcial del jugador


def generar_carta():
  cartas = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
  palos = ("♥", "♦", "♣", "♠")

  valor_carta = random.randint(1, 13) # Es representación de la carta ENTERO
  carta = cartas[valor_carta - 1] # Signo de la carta STRING
  palo = random.choice(palos) # Palo de la carta STRING

  # TUPLA: (VALOR CARTA, CARTA, PALO)
  return valor_carta, carta, palo


# INICIO
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
    