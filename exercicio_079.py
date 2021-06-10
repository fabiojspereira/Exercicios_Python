lista_anterior = lista = list()

continua = True
while continua == True :
	lista_anterior = lista[:]
	lista.append(int(input("Digite um valor para ser adicionado na lista : ")))

	item_atual = lista[len(lista)-1]

	if len(lista) > 1 :
		if lista[len(lista)-1] in lista_anterior :
			print("Valor já cadastrado anteriormente... ")
			lista.pop()
			#del lista[len(lista)-1]

		esc_01 = str(input("Deseja continuar o cadastro [ S / N ] ? ")).strip().lower()[0]
		if esc_01 == "s" :
			continua = True
		else:
			continua = False
	else:
		esc_01 = str(input("Deseja continuar o cadastro [ S / N ] ? ")).strip().lower()[0]
		if esc_01 == "s" :
			continua = True
		else:
			continua = False

print(f"\nForam digitados os seguintes valores : {sorted(lista)}")

# print (f"Tamanho da lista : {len(lista)}")
# print(f"Tamanho da lista -1 : {len(lista)-1}")
# print(f"ITEM ATUAL DA LISTA {lista[len(lista)-1]}")
# print(f"Lista : {lista}")
