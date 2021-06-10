tupla1 = tupla2 = tupla3 = tupla4 = ()
pares = []

# Uma forma de receber os 4 valores diretamente para a tupla :
#tupla = ( int(input(f"Digite o 1º valor a ser armazenado : ")), int(input(f"Digite o 1º valor a ser armazenado : ")),
#		  int(input(f"Digite o 1º valor a ser armazenado : ")),int(input(f"Digite o 1º valor a ser armazenado : ")))



tupla1 = int(input(f"Digite o 1º valor a ser armazenado : "))
if tupla1 % 2 == 0:
	pares.append(tupla1)

tupla2 = int(input(f"Digite o 2º valor a ser armazenado : "))
if tupla2 % 2 == 0:
	pares.append(tupla2)

tupla3 = int(input(f"Digite o 3º valor a ser armazenado : "))
if tupla3 % 2 == 0:
	pares.append(tupla3)

tupla4 = int(input(f"Digite o 4º valor a ser armazenado : "))
if tupla4 % 2 == 0:
	pares.append(tupla4)

tupla = tupla1, tupla2, tupla3, tupla4
print(f"\nNúmeros digitados : {tupla} ")
print(f"\nA quantidade de números 9 é de {tupla.count(9)}")

if 3 in tupla :
	print(f"O valor 3 foi digitado na {tupla.index(3)+1}º posição.")
else:
	print("Não foi digitado nenhum número 3.")
print(f"Números pares alocados : {pares}")


