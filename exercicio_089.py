print("\033[1;30;46m{:^40}\033[m".format("PROGRAMA BOLETIM 1.0"))

cadastro = list()

continua_001 = True
while continua_001 == True :

	nome = str(input("\nDigite o nome do aluno : ")).strip()
	n1 = float(input("Digite a primeira nota : "))
	n2 = float(input("Digite a segunda nota : "))

	media = (n1 + n2) / 2
	cadastro.append ( [ nome, [ n1, n2 ], media ] )

	continua_002 = True
	while continua_002 == True :
		esc_01 = str(input("\033[1;33mDeseja cadastrar outro aluno [ S / N ] ?\033[m ")).strip().lower()[0]
		if esc_01 in "s" :
			continua_001 = True
			continua_002 = False
		elif esc_01 in "n":
			continua_001 = False
			continua_002 = False
		else :
			print("Opção inválida !!! ")
			continua_002 = True

print(f"\n\033[1;30;46m{'Nº':<5}{'NOME DO ALUNO':<15}{'MÉDIA':<5}\033[m")
for count in range( 0, len(cadastro) ) :
	#print("{:<5}{:<15}{:<5}".format(count+1,cadastro[count][0],cadastro[count][2]))
	print(f'{count+1:^5}{cadastro[count][0]:^15}{cadastro[count][2]:^5}')

continua_003 = 0
while continua_003 != 999 :

	esc_02 = int(input("\nDeseja ver as notas de qual aluno ? 1 a {}.[ Digite 999 para sair ] : ".format(len(cadastro))))
	if esc_02 == 999 :
		continua_003 = 999
	elif 1 <= esc_02 <= len(cadastro) :
		print("Exibindo as notas de {} : Notas {}.".format(cadastro[esc_02 - 1][0], cadastro[esc_02 - 1][1]))
		continua_003 = 0
	else :
		print("Digite um valor válido !!!")
		continua_003 = 0

print("FIM DO PROGRAMA BOLETIM 1.0 ")
