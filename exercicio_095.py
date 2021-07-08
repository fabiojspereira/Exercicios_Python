dados_jogador = dict()

lista_jogadores = list()
lista_de_gols = list()

total_de_gols = 0

continua_001 = True
while continua_001 == True :
	dados_jogador ["nome"] = str(input("Digite o nome do jogador : ")).strip()
	QTD_partidas = int(input(f"Digite a quantidade de jogos que { dados_jogador['nome']} participou : "))

	for count in range ( 0, QTD_partidas ) :
		lista_de_gols.append(int(input(f"Digite a quantidade de gols na partida {count+1} : " )))
		total_de_gols = sum(lista_de_gols)
		dados_jogador ["gols"] = lista_de_gols[:]

	lista_de_gols.clear()
	dados_jogador ["total_gols"] = total_de_gols
	total_de_gols = 0
	lista_jogadores.append(dados_jogador.copy())

	continua_002 = True
	while continua_002 == True :
		esc_001 = str(input("\n\033[1;33mDeseja continuar o cadastro de jogadores [ S / N ] ?\033[m "))	.strip()[0].lower()
		if esc_001 == "s":
			continua_001 = True
			continua_002 = False
		elif esc_001 == "n":
			continua_001 = False
			continua_002 = False
		else :
			continua_002 = True
			print("\033[1;31mOpção inválida... Tente novamente.\033[m")

#print(lista_jogadores)
#print(lista_jogadores[0]['gols'])
#print(f"Quantidade de cadastros : {len(lista_jogadores)}")
print(f"\033[1;34m{'ITEM':<10}{'NOME':<10}{'GOLS POR PARTIDA':<20}{'TOTAL DE GOLS':<20}\033[m")

for count in range ( 0, len(lista_jogadores)) :
	format_list_exib = str(lista_jogadores[count]["gols"])
	print(f"{count+1:<10}{lista_jogadores[count]['nome']:<10}{format_list_exib:<20}{lista_jogadores[count]['total_gols']}")

continua_003 = True
while continua_003 == True :
	mostrar_dados_jogador = int(input(f"\nDeseja mostrar dados de qual jogador [ 1 - {len(lista_jogadores)} ] [ \033[1;33m999 = sair\033[m ] ? "))

	if mostrar_dados_jogador <= len(lista_jogadores) and mostrar_dados_jogador > 0 :
		print(f"\nLevantamento de dados do jogador {lista_jogadores[mostrar_dados_jogador - 1]['nome']} :")
		for indice, valor in enumerate(lista_jogadores[mostrar_dados_jogador - 1]['gols']):
			print(f"No jogo {indice + 1} fez {valor} gols.")

	elif mostrar_dados_jogador == 999 :
		continua_003 = False

	else :
		print("\033[1;31mOpção inválida... Tente novamente.\033[m")

print("PROGRAMA FINALIZADO")
