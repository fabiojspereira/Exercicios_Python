lista_temporaria = list()
cadastro = list()

lista_pesados = list()
lista_leves = list()

total_pessoas = 0
peso_maior = peso_menor = 0

continua = continua_02 = True

while continua == True:
	lista_temporaria.append(str(input("Digite o nome da pessoa : ")).strip())
	lista_temporaria.append(int(input("Digite o peso : ")))
	cadastro.append(lista_temporaria[:])
	lista_temporaria.clear()  # ou lista_temporaria.pop(0) lista_temporaria.pop(0)
	# print(f"último nome cadastrado : {cadastro[len(cadastro) - 1][0]}")
	# print(f"último peso cadastrado : {cadastro[len(cadastro) - 1][1]}")

	total_pessoas = total_pessoas + 1

	if total_pessoas == 1:
		peso_maior = peso_menor = cadastro[0][1]
		lista_pesados.append(cadastro[len(cadastro) - 1][0])
		lista_leves.append(cadastro[len(cadastro) - 1][0])

	elif cadastro[len(cadastro) - 1][1] == peso_maior:  		# comparando o peso do último cadastro fornecido com o PESO MAIOR
		lista_pesados.append(cadastro[len(cadastro) - 1][0])	# append pelo NOME que é o índice [ 0 ]
		peso_maior = cadastro[len(cadastro) - 1][1]				# append pelo PESO que é o índice [ 1 ]

	elif cadastro[len(cadastro) - 1][1] > peso_maior:
		lista_pesados.clear()									# quando temos um PESO MAIOR que o atual, limpamos a lista.
		lista_pesados.append(cadastro[len(cadastro) - 1][0])	# append pelo NOME que é o índice [ 0 ]
		peso_maior = cadastro[len(cadastro) - 1][1]				# append pelo PESO que é o índice [ 1 ]

	elif cadastro[len(cadastro) - 1][1] == peso_menor:
		lista_leves.append(cadastro[len(cadastro) - 1][0])
		peso_menor = cadastro[len(cadastro) - 1][1]

	elif cadastro[len(cadastro) - 1][1] < peso_menor:
		lista_leves.clear()
		lista_leves.append(cadastro[len(cadastro) - 1][0])
		peso_menor = cadastro[len(cadastro) - 1][1]

	continua_02 = True
	while continua_02 == True:
		esc_01 = input("Deseja cadastrar outra pessoa [ S / N ] : ").lower()[0:1]
		if esc_01 == "s":
			continua = True
			continua_02 = False
		elif esc_01 == "n":
			continua = False
			continua_02 = False
		else:
			print("opção inválida ... ")
			continua_02 = True

print(f"\nTotal de pessoas cadastradas : {total_pessoas} ")
print(f"\nO maior peso cadastrado foi de : {peso_maior} Kg.")
print(f"O menor peso cadastrado foi de : {peso_menor} Kg.")

print(f"\nPessoas com o maior peso : {lista_pesados}")
print(f"Pessoas com o menor peso : {lista_leves}")
