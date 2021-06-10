media_idade = 0
nome_homem_velho = ""
idade_homem_velho = 0
mulheres_jovens = 0

for pessoa in range (0,4):
	nome = str(input("\nDigite o nome da {}º pessoa : ".format(pessoa + 1)).strip())
	idade = int(input("Digite a idade da {}º pessoa : ".format(pessoa + 1)))
	sexo = str(input("Digite o sexo da {}º pessoa : ".format(pessoa + 1))).strip().lower()

	media_idade = media_idade + idade  # Servirá para calcular a média final.

	if sexo == "masculino" or sexo == "m":
		if idade > idade_homem_velho:
			nome_homem_velho = nome
			idade_homem_velho = idade

	if sexo == "feminino" or sexo == "f":
		if idade < 20:
			mulheres_jovens = mulheres_jovens + 1

print("\nA média de idade do grupo é de : {} anos.".format(media_idade/4))
print("O nome do homem mais velho é : {}, com {} anos de idade.".format(nome_homem_velho,idade_homem_velho))
print("A quantidade de mulheres com menos de 20 anos de idade é : {}.".format(mulheres_jovens))
