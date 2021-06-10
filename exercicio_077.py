palavras = ("casa", "carro", "bicicleta", "computador", "paralelepipedo", "apartamento", "praia", "sofa", "cachorro")

vogais = ("a", "e", "i", "o", "u")

vogais_presentes = []

for count in range(0, len(palavras)):
	print("\nNa palavra \033[1;33m{}\033[m temos as seguintes vogais : ".format(palavras[count].upper()), end="")
	item = (palavras[count])
	vogais_presentes = []
	for count in range(0, len(item)):
		if item[count] in vogais : #and item[count] not in vogais_presentes: # Este complemento define a repetição ou não das vogais exibidas.
			vogais_presentes.append(item[count])
	print("\033[1;34m",vogais_presentes,"\033[m",end=" ")

