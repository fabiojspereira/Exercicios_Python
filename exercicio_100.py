import random
from time import sleep

lista_de_numeros = list()
lista_de_numeros_sorteados = list()

# Criação do universo de sorteio
for contador in range(0, 101, 1):
	lista_de_numeros.append(contador)


def sorteio():
	print(f"Sorteando 5 valores do universo criado : ", end="")
	for contador in range(0, 5):
		numero_sorteado = random.choice(lista_de_numeros)
		lista_de_numeros_sorteados.append(numero_sorteado)
		sleep(0.25)
		print(f"\033[1;34m{numero_sorteado}\033[m", end=" ")


def soma_par():
	numero_par = 0
	for contador in lista_de_numeros_sorteados:
		if contador % 2 == 0:
			numero_par = numero_par + contador
	print(
		f"\nA soma dos valores pares da lista de números sorteados : "
		f"\033[1;31m{lista_de_numeros_sorteados}\033[m é \033[1;32m{numero_par}\033[m."
	)


# Sorteio de 5 números dentro do universo criado
sorteio()
soma_par()
