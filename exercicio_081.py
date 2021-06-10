lista = list()
continua = True

while continua == True:
	lista.append(int(input("Digite um valor para ser adicionado à lista : ")))
	esc_01 = str(input("Deseja continuar o processo [ S / N ] ? ")).strip().lower()[0]
	if esc_01 == "s":
		continua = True
	else:
		continua = False

print(f"\nA quantidade de números digitados foi : {len(lista)}")
lista.sort(reverse=True)
print(f"A lista ordenada de forma descrescente é : {lista}")
if 5 in lista:
	print("O número cinco ( 5 ) foi digitado e está na lista.")
else:
	print("O número cinco ( 5 ) não foi incluído nesta lista.")
