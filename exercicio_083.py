parenteses = []

exp = str(input("Digite a expressão : ")).strip()

for char in range ( 0 , len(exp)) :
	if exp[char] == "(" :
		parenteses.append("(")
	elif exp[char] == ")" :
		if len(parenteses) > 0 :
			parenteses.pop()
		else :
			parenteses.append(")")
			break

if len(parenteses) == 0 :
	print(f"\nA expressão {exp} é verdadeira !")
else :
	print(f"A expressão {exp} é falsa !")



'''
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
