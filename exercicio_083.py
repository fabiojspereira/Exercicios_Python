parenteses = []
erro = False

while True:
	exp = str(input("Digite a expressão : ")).strip()

	for char in range(0, len(exp)):
		if exp[0] == ")":
			print("ERROR")
			erro = True
			break

		if exp[char] == "(":
			parenteses.append("(")
		elif exp[char] == ")":
			if len(parenteses) > 0:
				parenteses.pop()
			else:
				parenteses.append(")")
				break

	if erro == False:
		if len(parenteses) == 0:
			print(f"\nA expressão {exp} é verdadeira !\n")
		else:
			print(f"A expressão {exp} é falsa !\n")
		parenteses = []  # É necessário limpar a lista neste ponto.
	else:
		break



'''
parenteses = []
continua = True

while continua == True:
	exp = str(input("Digite a expressão : ")).strip()
	if exp[0] == ")":
		print("Expressão iniciou de forma indevida.")
		continua = False

	for char in range(0, len(exp)):
		if exp[char] == "(":
			parenteses.append("(")
		elif exp[char] == ")":
			if len(parenteses) > 0:
				parenteses.pop()
			else:
				parenteses.append(")")
				break
	continua = True

	if len(parenteses) == 0:
		print(f"\nA expressão {exp} é verdadeira !\n")
	else:
		print(f"A expressão {exp} é falsa !\n")
	parenteses = []  # É necessário limpar a lista neste ponto.




(a*b)-)c(=12



exp = str(input("Digite a expressão : ")).strip()
pilha = []

for char in exp :
	if char == "(" :
		pilha.append("(")
	elif char == ")" :
		if len(pilha) > 0 :
			pilha.pop()
		else :
			pilha.append(")")
			break

if len(pilha) == 0 :
	print(f"\nA expressão {exp} é verdadeira !")
else :
	print(f"A expressão {exp} é falsa !")
'''
