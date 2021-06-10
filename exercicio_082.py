lista = list()
lista_par = list()
lista_impar = list()

continua_01 = continua_02 = True
par = impar = 0

while continua_01 == True :
	continua_02 = True
	lista.append(int(input("Digite um valor para ser adicionado à lista : ")))
	while continua_02 == True :
		esc_01 = str(input("Deseja continuar [ S / N ] ? ")).strip().lower()[0]
		if esc_01 == "s" :
			continua_02 = False
		elif esc_01 == "n" :
			continua_02 = continua_01 = False
		else :
			print("Opção inválida ! Tente novamente ...")

for count in range ( 0, len(lista) ) :
	print(f"{lista[count]}",end=" ")
	if lista[count] % 2 == 0 :
		lista_par.append(lista[count])
		par += 1
	else :
		lista_impar.append(lista[count])
		impar += 1

print(f"\nLista completa : {lista}")
print(f"Lista com {par} ítens pares : {lista_par}")
print(f"Lista com {impar} ítens ímpares : {lista_impar}")
