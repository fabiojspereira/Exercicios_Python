lista = []
lista_maior = []
lista_menor = []

for count in range ( 0, 5 ) :
	lista.append(int(input(f"Digite um valor para a posição {count+1} : ")))
	if count == 0 :
		maior = menor = lista[0]
	if lista[count] == maior :
		lista_maior.append(count+1)
	elif lista[count] > maior :
		lista_maior = list()
		maior = lista[count]
		lista_maior.append(count + 1)
	if lista[count] == menor :
		lista_menor.append(count+1)
	elif lista[count] < menor :
		lista_menor = list()
		menor = lista[count]
		lista_menor.append(count+1)
print(f"\nOs valores digitados foram : {lista}")
print(f"O maior valor digitado foi {maior}. Apareceu nas posições : ",end="")
for count in lista_maior :
	print(f"{count}... ",end="")
print(f"\nO menor valor digitado foi {menor}. Apareceu nas posições : ",end="")
for  count in lista_menor :
	print(f"{count}... ",end="")
