qtd_h = qtd_pessoa = qtd_pessoas_maior = mulheres_jovens = 0

continua = True
while continua == True:

	controle_01 = False
	while controle_01 == False:
		idade = input("Digite a idade da {}º pessoa : ".format(qtd_pessoa + 1))
		if idade.isdigit() == True:
			idade = int(idade)
			controle_01 = True
		else:
			print("\033[1;31mOpção inválida. Tente novamente.\n\033[m")
			controle_01 = False

	controle_02 = False
	while controle_02 == False:
		sexo = str(input(f"Digite o sexo da {qtd_pessoa + 1}º pessoa [ M / F ] : ")).strip().lower()[0:1]
		if sexo == "m":
			controle_02 = True
			qtd_pessoa = qtd_pessoa + 1
			qtd_h = qtd_h + 1
			if idade > 18:
				qtd_pessoas_maior = qtd_pessoas_maior + 1
		elif sexo == "f":
			controle_02 = True
			qtd_pessoa = qtd_pessoa + 1
			if idade < 20:
				mulheres_jovens = mulheres_jovens + 1
			if idade > 18:
				qtd_pessoas_maior = qtd_pessoas_maior + 1
		else:
			controle_02 = False
			print("\033[1;31mOpção inválida. Tente novamente.\n\033[m")
			#break

	controle_03 = False
	while controle_03 == False:
		esc_01 = str(input("\n\033[1;33mDeseja continuar o cadastro [ S / N ] ?\033[m ")).strip().lower()[0:1]
		if esc_01 == "s":
			continua = True
			controle_03 = True
		elif esc_01 == "n":
			continua = False
			controle_03 = True
		else:
			controle_03 = False
			print("\033[1;31mOpção inválida. Tente novamente.\n\033[m")

print("\nQuantidade de cadastrados : {}.".format(qtd_pessoa))
print(f"A quantidade de pessoas que tem mais de 18 anos de idade é : {qtd_pessoas_maior}.")
print(f"A quantidade de homens cadastrados foi de : {qtd_h}.")
print(f"A quantidade de mulheres com menos de 20 anos de idade é : {mulheres_jovens}.")

'''
controle_01 = False
while controle_01 == False:
	idade = input("\nDigite a idade da {}º pessoa : ".format(qtd_pessoa + 1))
	count_01 = len(idade)
	print(count_01)
	for c in range(0, count_01, 1):  # Lembrando que o último não conta.
		print(f"\n{idade[c]}", end=" ")
		tipo_var = type(idade[c])
		print(tipo_var)
		if tipo_var == int:
			# print(f"{type(idade[c])}",end="")
			# print(f"Caractere {idade[c]} :",end=" ")
			print("É um número")
			c = c + 1
		# controle = True

		elif tipo_var == str:
			# print(f"POSIÇÃO {idade[c]}",end=" ")
			# print("Não é um número")
			c = c + 1
			print("É uma letra.")
	# print("\033[1;31mOpção inválida. Tente novamente.\033[m")
	# controle = False
'''
'''
controle_01 = False
while controle_01 == False:
	idade = input("\nDigite a idade da {}º pessoa : ".format(qtd_pessoa + 1))
	count_01 = len(idade)
	for c in range(0, count_01, 1):  # Lembrando que o último não conta.
		print(f"\n{idade[c]}", end=" ")
		caractere = c
		if idade[c].isdigit() == True:
			print("É um número")
			c = c + 1

		elif idade[c].isalpha() == True:
			c = c + 1
			print("É uma letra.")
'''
