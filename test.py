import random

def generar_carta():
  cartas = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
  palos = ("♥", "♦", "♣", "♠")

  valor_carta = random.randint(1, 13) # Es representación de la carta ENTERO
  carta = cartas[valor_carta - 1] # Signo de la carta STRING
  palo = random.choice(palos) # Palo de la carta STRING

  # TUPLA: (VALOR CARTA, CARTA, PALO)
  return valor_carta, carta, palo

print(generar_carta())

# Test: python ./test.py