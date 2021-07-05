registro = dict()
cadastro_geral = list()

QTD_mulher = QTD_cadastro = media_idade = soma_idade = 0

continua_geral = True
while continua_geral == True:

	registro["nome"] = str(input("Digite o nome : ")).strip()

	continua_001 = True
	while continua_001 == True:
		registro["sexo"] = str(input("Digite o sexo [ M / F ] : ")).strip()[0].lower()
		if registro["sexo"] not in "mf":
			print("Opção inválida ! Tente novamente...")
			continua_001 = True
		elif registro["sexo"] == "f":
			QTD_mulher += 1
			continua_001 = False
		else:
			continua_001 = False

	continua_002 = True
	while continua_002 == True:
		registro["idade"] = str(input("Digite a idade : "))
		if registro["idade"].isnumeric() == True:
			continua_002 = False
		else:
			continua_002 = True
			print("Opção inválida ! Tente novamente...")

	QTD_cadastro += 1
	registro["idade"] = float(registro["idade"])
	soma_idade = soma_idade + registro["idade"]
	media_idade = soma_idade / QTD_cadastro

	continua_003 = True
	while continua_003 == True:
		esc_001 = str(input("Deseja continuar o cadastro [ S / N ] : ")).strip()[0].lower()
		if esc_001 in "s":
			continua_003 = False
			continua_geral = True
		elif esc_001 in "n":
			continua_003 = False
			continua_geral = False
		else:
			continua_003 = True
			print("Opção inválida ! Tente novamente...")

	cadastro_geral.append(registro.copy())  # forma de alimentar uma LISTA com dicionários.

print()
print(f"A quantidade de pessoas cadastradas foi de : {QTD_cadastro}.")
print(f"A média de idade do grupo cadastrado é : {media_idade:.2f} anos.")
print(f"A quantidade de mulheres é de : {QTD_mulher}.")
print("As mulheres cadastradas foram : ", end="")
for count in range(0, len(cadastro_geral)):
	if cadastro_geral[count]["sexo"] == "f":
		print(cadastro_geral[count]['nome'],end="-")

print()
print("FIM DO PROGRAMA")
