import datetime
nome = str(input("Cidadão, digite seu nome : ")).strip()
sexo = str(input("Digite seu sexo : ")).strip()
nascimento = int(input("\nPrezado {}, vamos verificar sua situação junto ao serviço militar.\nDigite o seu ano de ""nascimento : ".format(nome)))

ano_atual = datetime.date.today().year
serv_mil = 18
idade = ano_atual - nascimento

#print(sexo.upper())

if sexo.upper() == "MASCULINO" or sexo.upper() == "M":
	if idade < 18:
		print ("{}, ainda não está na hora de se alistar ao serviço militar.\nFaltam {} ano(s).".format(nome,serv_mil-idade))
	elif idade == 18:
		print("Atenção cidadão ! Neste ano de {}, você precisa fazer seu alistamento militar !".format(ano_atual))
	else:
		print("{}, você já passou do tempo de alistamento.\nIsso foi há {} ano(s).".format(nome,idade-serv_mil))
else:
	print("\nCidadão do sexo feminino não têm a obrigatoriedade de alistamento no serviço militar.")
