numero = int(input("\nDigite um número inteiro para saber se é um número primo : "))

qtd_div = 0

for count in range (1, numero+1, 1):
	if numero % count == 0:
		print("\033[7;32m{}\033[m".format((count)), end =" -> ")
		qtd_div = qtd_div + 1
	else:
		print("\033[1;37m{}\033[m".format((count)), end =" -> ")

print("\n\nO número {} foi divisível {} vez(es).".format(numero, qtd_div))

if qtd_div == 2:
	print("E por isso ele é um número primo.")
else:
	print("E por isso ele não é um número primo.")

# Minha solução principal :
''' 
numero = int(input("\nDigite um número inteiro para saber se é um número primo : "))
for count in range (0,1): # 1,2,3
	if numero == 1:
		print("O número 1 não é primo.")
	elif numero == 2:
		print("O número 2 é primo.")
	else:
		if numero % 2 == 0:
			print("O número {} não é primo.".format(numero))
		elif numero % 3 == 0:
			print("O número {} não é primo.".format(numero))
		else:
			print("O número {} é primo.".format(numero))
'''
