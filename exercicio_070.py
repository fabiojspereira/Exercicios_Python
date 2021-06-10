total_gasto = 0
prod_1000 = 0
nome_prod_barato = ""
valor_prod_barato = 0

count = 0

continua = True
while continua == True:

	nome_prod = str(input("\nDigite o nome do produto : "))
	val_prod = float(input("Digite o valor do produto : "))

	total_gasto = total_gasto + val_prod

	if val_prod > 1000:
		prod_1000 = prod_1000 + 1

	if count == 0:
		nome_prod_barato = nome_prod
		valor_prod_barato = val_prod
		count = count + 1
	else:
		if val_prod < valor_prod_barato:
			valor_prod_barato = val_prod
			nome_prod_barato = nome_prod


	controle_01 = False
	while controle_01 == False:
		esc_01 = str(input("Deseja cadastrar mais produtos [ S / N ] ? ")).strip().lower()[0:1]

		if esc_01 == "s":
			controle_01 = True
			continua = True

		elif esc_01 == "n":
			controle_01 = True
			continua = False
		else:
			controle_01 = False
			print("Opção inválida. Tente novamente.")

print(f"\nTotal gasto na compra : {total_gasto:.2f}")
print(f"Produtos que custam acima de R$1.000,00 : {prod_1000}")
print(f"Produto mais barato : {nome_prod_barato} - R$ {valor_prod_barato:.2f}")
