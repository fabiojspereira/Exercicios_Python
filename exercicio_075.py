tupla = tuple()
numeros_pares = list()

tupla = (
	int(input("Digite um valor : ")),
	int(input("Digite um valor : ")),
	int(input("Digite um valor : ")),
	int(input("Digite um valor : "))
	)

print(f"A tupla foi criada : {tupla}")

count_temp = 0
contador = 0
check = True
for valor in range (0, len(tupla)):
	if tupla[valor] == 9:
		#print(f"{tupla[valor]}. Numero 9 digitado...")
		contador += 1

	if (tupla[valor]) % 2 == 0:
		#print(f"{tupla[valor]}. Numero par digitado...")
		numeros_pares.append(tupla[valor])

	while check == True:
		count_temp += 1
		#print(f"ENTREI NO WHILE PELA {count_temp}º VEZ...")
		if tupla[valor] == 3:
			#print(f"{tupla[valor]}. Numero 3 digitado...")
			pos_num_3 = valor
			check = False
			break

		else:
			#print(f"{tupla[valor]}. Numero qualquer digitado... foda-se...")
			check = True
			break

print(f"\nQuantidade de números 9 digitados é de : {contador} vez(es).")
#print(f"\nA quantidade de números 9 é de {tupla.count(9)}")
print(f"\nQuantidade de números pares digitados : {len(numeros_pares)}")
print(f"Listagem de números pares digitados : {numeros_pares}")

if check == True:
	print(f"\nO valor 3 não foi digitado em nenhum momento ....")
else:
	print(f"\nO valor 3 foi digitado primeiramente na {pos_num_3 + 1}º posição.")
