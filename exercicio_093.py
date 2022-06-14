dados_jogador = dict()
lista_de_gols = list()
total_de_gols = 0

dados_jogador ["Nome"] = str(input("Digite o nome do jogador : ")).strip()
# dados_jogador ["QTD_partidas"] = int(input(f"Digite a quantidade de jogos que { dados_jogador['Nome']} participou : "))
QTD_partidas = int(input(f"Digite a quantidade de jogos que { dados_jogador['Nome']} participou : "))

for count in range ( 0, QTD_partidas ) :
	lista_de_gols.append(int(input(f"Digite a quantidade de gols na partida {count+1} : " )))
	dados_jogador ["gols"] = lista_de_gols[:]

dados_jogador ["total_gols"] = sum(lista_de_gols)

print(dados_jogador)
print()

for chave, valor in dados_jogador.items() :			# Estrutura que percorre os dados dentro do dicionário
	print(f"O campo {chave} tem o valor {valor}.")	# Estrutura que percorre os dados dentro do dicionário

print()
print(f"O jogador {dados_jogador ['Nome']}, participou de {QTD_partidas} partidas.")
for count in range ( 0, QTD_partidas ) :
	print(f"Na {count+1}° partida fez {lista_de_gols[count]} gol(s).")
print(f"\nFoi um total de {dados_jogador ['total_gols']} gol(s)")

"""
dados_jogador = dict()
lista_de_gols = list()
total_de_gols = 0

dados_jogador ["nome"] = str(input("Digite o nome do jogador : ")).strip()
dados_jogador ["qtd_partidas"] = int(input(f"Digite a quantidade de partidas que o jogador {dados_jogador ['nome'] } participou : "))

lista_de_gols = list(range(0, dados_jogador["qtd_partidas"]))  # Criação da lista com a quantidade de itens.

for partida in range (0, dados_jogador["qtd_partidas"]):
	lista_de_gols[partida] = int(input(f"Digite a quantidade de gols na partida {partida+1} : "))

dados_jogador["gols"] = lista_de_gols
total_de_gols = sum(dados_jogador["gols"])
dados_jogador ["total_gols"] = total_de_gols

print(f"{dados_jogador}\n")

for k,v in dados_jogador.items():
	print(f"O campo {k}, tem o valor : {v}")
"""
