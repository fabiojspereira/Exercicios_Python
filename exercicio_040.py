x = len("Programa para cálculo de média")
print("*"*x)
print("Programa para cálculo de média")
print("*"*x)

n1 = float(input("\nDigite a primeira nota do aluno : "))
n2 = float(input("Digite a segunda nota do aluno : "))

m = ( n1 + n2 ) / 2

if m < 5.0:
	print("O aluno está \033[1;31mreprovado\033[m. Média abaixo de 5.0 : {:.1f}".format(m))
elif m >= 5.0 and m <= 6.9:
	print("O aluno está em \033[1;33mrecuperação\033[m. Média entre 5.0 e 6.9 : {:.1f}".format(m))
elif m >= 7.0:
	print("Aluno \033[1;32maprovado !\033[m Média igual ou superior à 7.0 : {:.1f}".format(m))
