import random

def generar_carta():
  cartas = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
  palos = ("♥", "♦", "♣", "♠")

  valor_carta = random.randint(1, 13) # Es representación de la carta ENTERO
  carta = cartas[valor_carta - 1] # Signo de la carta STRING
  palo = random.choice(palos) # Palo de la carta STRING

  # TUPLA: (VALOR CARTA, CARTA, PALO)
  return valor_carta, carta, palo


# Dada una carta y el puntaje actual, retorna el puntaje de la carta
def puntaje_carta(carta, puntaje_actual):
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


puntaje = 0

carta1 = generar_carta()
carta2 = generar_carta()

print("1er)", carta1)
puntaje += puntaje_carta(carta1, puntaje)
print("Puntaje:", puntaje)

print("2da)", carta2)
puntaje += puntaje_carta(carta2, puntaje)
print("Puntaje:", puntaje)

print
# Test: python ./test.py
"""
1er) (4, '4', '♣')
Puntaje: 4
2da) (13, 'K', '♦')
Puntaje: 14


----------

1er) (1, 'A', '♣')
Puntaje: 11
2da) (13, 'K', '♠')
Puntaje: 21
"""