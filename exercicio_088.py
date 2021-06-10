from time import sleep
from random import randrange

print("\033[1;30;46m{:^50}\033[m".format("PROGRAMA PARA SORTEIO DE NÚMEROS DA MEGA-SENA"))
qtd_jogos = int(input("\nDigite a quantidade de jogos a serem sorteados : "))

jogo_criado = list()
lista_de_jogos = list()
duplicados = list()
check_color = False

print()
for count_01 in range(0, qtd_jogos):

	for count_02 in range(0, 6):
		numero_sorteado = randrange(1, 61, 1)
		#print(f"O {count_02+1}º número sorteado foi : {numero_sorteado}")

		check_equal = True
		while check_equal == True :
			if numero_sorteado in jogo_criado :
				duplicados.append(numero_sorteado)
				print("\033[1;30;41m Jogo {:^3} \033[m : Número [ \033[1;31m{}\033[m ] duplicado. Gerando novo número : ".format(count_01+1,numero_sorteado),end="")
				numero_sorteado = randrange(1, 61, 1)
				print(f"[ \033[1;32m{numero_sorteado}\033[m ]")
				check_equal = True
				check_color = True
			else :
				#print(f"Número válido adicionado : {numero_sorteado}")
				jogo_criado.append(numero_sorteado)
				check_equal = False

	lista_de_jogos.append(jogo_criado[:]) # listagem contendo todos os jogos gerados. Sem uso por enquanto.
	sleep(0.35)
	#jogo_criado.sort()
	if check_color == True :
		print("\033[1;30;42m Jogo {:^3} \033[m : \033[0;32m{}\033[m".format(count_01+1, jogo_criado))
		check_color = False
	elif check_color == False :
		print("\033[1;30;46m Jogo {:^3} \033[m : \033[0;32m{}\033[m".format(count_01+1, jogo_criado))
		check_color = False

	jogo_criado.clear()

print("\n\033[1;30;46m          \033[m : Jogo gerado sem duplicidade de números.")
print("\033[1;30;41m          \033[m : Jogo gerado com duplicidade de 1 ou mais números.")
print("\033[1;30;42m          \033[m : Jogo corrigido.")
print("\nListagem de jogos gerada ! Boa sorte !")
