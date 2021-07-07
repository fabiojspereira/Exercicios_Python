dados_jogador = dict()
lista_de_gols = list()
total_de_gols = 0

dados_jogador ["Nome"] = str(input("Digite o nome do jogador : ")).strip()
# dados_jogador ["QTD_partidas"] = int(input(f"Digite a quantidade de jogos que { dados_jogador['Nome']} participou : "))
QTD_partidas = int(input(f"Digite a quantidade de jogos que { dados_jogador['Nome']} participou : "))

for count in range ( 0, QTD_partidas ) :
	QTD_gols = int(input(f"Digite a quantidade de gols na partida {count+1} : " ))
	lista_de_gols.append(QTD_gols)
	total_de_gols += QTD_gols
	dados_jogador ["gols"] = lista_de_gols[:]

dados_jogador ["total_gols"] = total_de_gols

print()
print(dados_jogador)
print()

for chave, valor in dados_jogador.items() :			# Estrutura que percorre os dados dentro do dicionário
	print(f"O campo {chave} tem o valor {valor}.")	# Estrutura que percorre os dados dentro do dicionário

print()
print(f"O jogador {dados_jogador ['Nome']}, participou de {QTD_partidas} partidas.")
for count in range ( 0, QTD_partidas ) :
	print(f"Na {count+1}° partida fez {lista_de_gols[count]} gol(s).")
print(f"\nFoi um total de {dados_jogador ['total_gols']} gol(s)")
