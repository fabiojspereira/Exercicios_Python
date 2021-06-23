from datetime import date

data_atual = date.today().year

maior_idade = 0
menor_idade = 0

for pessoa in range (0,7):
	ano = int(input("Digite o ano de nascimento da {}º pessoa : ".format(pessoa + 1)))
	idade = data_atual - ano
	if idade <= 21:
		maior_idade = maior_idade + 1
	elif ano > 21:
		menor_idade = menor_idade + 1

print("\nA quantidade de pessoas maiores de idade é : {}".format(maior_idade))
print("A quantidade de pessoas menores de idade é : {}".format((menor_idade)))
