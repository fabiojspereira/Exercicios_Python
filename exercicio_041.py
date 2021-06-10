import datetime
x = len("Confederação Nacional de Natação - CNN")
print("*"*x)
print("Confederação Nacional de Natação - CNN")
print("*"*x)

nome = str(input("\nDigite o nome do atleta : ")).strip()
ano_nasc = int(input("Digite o ano de nascimento do atleta : "))
idade = ( datetime.date.today().year - ano_nasc )

if idade <= 9:
	print("\nO aluno {}, tem {} anos de idade e faz parte da categoria : \033[1;34mMirim\033[m ".format(nome,idade))
elif idade <= 14 and idade > 9:
	print("\nO aluno {}, tem {} anos de idade e faz parte da categoria : \033[1;34mInfantil\033[m".format(nome,idade))
elif idade <= 19 and idade > 14:
	print("\nO aluno {}, tem {} anos de idade e faz parte da categoria : \033[1;34mJunior\033[m".format(nome,idade))
elif idade == 20:
	print("\nO aluno {}, tem {} anos de idade e faz parte da categoria : \033[1;34mSênior\033[m".format(nome,idade))
else:
	print("\nO aluno {}, tem {} anos de idade e faz parte da categoria : \033[1;34mMaster\033[m".format(nome,idade))



