from random import randint
from time import sleep
from operator import itemgetter

ranking = list()

sorteio = {"jogador 01": randint(1, 6),
		   "jogador 02": randint(1, 6),
		   "jogador 03": randint(1, 6),
		   "jogador 04": randint(1, 6) }

for chave, valor in sorteio.items() :
	sleep(0.5)
	print(f"O { chave } sorteou o número { valor }")

ranking = sorted(sorteio.items() , key=itemgetter(1), reverse=True)
print(ranking)
print()

for indice, valor in enumerate(ranking) :
	print(f"{indice+1}º lugar : {valor[0]} com o valor {valor[1] }")
