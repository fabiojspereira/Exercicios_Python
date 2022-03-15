from time import sleep

def maior_numero (* numeros):
	print()
	print("*" * 80)
	print("ANALISANDO OS VALORES PASSADOS ...")
	qtd_numeros = len(numeros)

	print(f"Os seguintes números foram passados : ", end="")
	if qtd_numeros == 0:
		print(end="\033[1;31m FIM DA LISTA\033[m")

	contador = 1
	for valor in numeros:
		sleep(0.25)
		if contador < len(numeros):
			print(f"\033[1;34m{valor}\033[m", end=", ")
			contador += 1
		else:
			print(f"\033[1;34m{valor}\033[m", end="\033[1;31m FIM DA LISTA\033[m")
			contador += 1

	print(f"\nTotalizando : {len(numeros)} números.")

	valor_maior = 0
	for valor in range(0, len(numeros)):
		valor_atual = numeros[valor]
		if valor_atual >= valor_maior:
			valor_maior = valor_atual

	print(f"O maior número é : {valor_maior}")
	print("*" * 80)

maior_numero(12, -1, 2, 23, 0, 7, 8, 9, 12)
maior_numero(101,54, 56, 1, 27, 55, 100)
maior_numero(2, 3)
maior_numero(15)
maior_numero(-2, -1, 0)
maior_numero(1)
maior_numero()
