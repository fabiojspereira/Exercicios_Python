from time import sleep

x = len("PROGRAMA DE EMPRÉSTIMOS BANCÁRIOS E FINANCIAMENTOS")
print("*"*x)
print("PROGRAMA DE EMPRÉSTIMOS BANCÁRIOS E FINANCIAMENTOS")
print("*"*x)
nome = str(input("\nNome completo do comprador ou solicitante do empréstimo : ")).strip()
valor = float(input("Digite o valor requerido : "))
salario = float(input("Digite o valor do salário do solicitante : "))
tempo_ano = int(input("Digite a quantidade de anos para a quitação da dívida : "))

print("\nCalculando parametros necessários ...")
sleep(0.5)
prestacao_mensal = ( valor / tempo_ano ) / 12
print("\nA prestacão mensal em nossa empresa para a sua solicitação será de : \033[33mR$ {:.2f}\033[m".format(prestacao_mensal))
print ("\033[1;34mQuantidade de anos :\033[m {} ano(s).\n\033[1;34mQuantidade de meses :\033[m {} mese(s).\n".format(tempo_ano,tempo_ano * 12))
print(f"\nCoeficiente : {prestacao_mensal/salario:.3f}\nPara o empréstimo ser aceito o coeficiente precisa ser menor que 0.30.")
print(f"Valor máximo da prestação para ser aceito precisa ser menor que R$ {salario * 0.3:.2f}")

if prestacao_mensal >= ( salario * 30 ) / 100:
	print("\n{}, infelizmente a prestação mensal será de \033[4;31m30%\033[m ou mais do seu salário. \nO Empréstimo foi \033[1;31mnegado.\033[m".format(nome))
elif prestacao_mensal < ( salario * 30 ) / 100:
	print("\nParabéns ! {}, sua solicitação foi \033[1;32maprovada.\033[m".format(nome))
