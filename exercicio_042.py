x = len("Vamos testar a existência de um triângulo e classifica-lo !")
print("*" * x)
print("Vamos testar a existência de um triângulo e classifica-lo !")
print("*" * x)

reta_01 = float(input("\nDigite o tamanho da reta 01 : "))
reta_02 = float(input("Digite o tamanho da reta 02 : "))
reta_03 = float(input("Digite o tamanho da reta 03 : "))


if (reta_02 - reta_03) < reta_01 < (reta_02 + reta_03) and (reta_01 - reta_03) < reta_02 < (reta_01 + reta_03) and (reta_01 - reta_02) < reta_03 < (reta_01 + reta_02):
	print("\nCom estas medidas {}, {} e {}, \033[1;34mé possível\033[m que exista um triângulo.".format(reta_01, reta_02, reta_03))
	if reta_01 == reta_02 == reta_03:
		print("\nO triângulo é equilátero.")
	elif ( reta_01 == reta_02 ) or ( reta_01 == reta_03 ) or ( reta_02 == reta_03 ):
		print("\nO triângulo é isósceles.")
	elif ( reta_01 != reta_02 ) and ( reta_02 != reta_03 ):
		print("\nO triângulo é escaleno.")
else:
	print("\nCom estas medidas {}, {} e {}, \033[1;31mnão é possível\033[m que venha a existir um triângulo.".format(reta_01, reta_02, reta_03))
	existe = "falso"