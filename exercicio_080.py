lista = list()
c = 0

for count in range( 0, 5 ) :
	lista.append(int(input(f"Digite o {count+1}º número da lista : ")))
	#item_atual = lista[len(lista)-1] ou lista[-1]

for count in range( 0, 5 ) :

	if count == c :
		if lista[4] < lista[3] :
			lista.insert( 3 , lista[4] )
			lista.pop(5)
		if lista[3] < lista[2] :
			lista.insert( 2 , lista[3] )
			lista.pop(4)
		if lista[2] < lista[1] :
			lista.insert( 1 , lista[2] )
			lista.pop(3)
		if lista[1] < lista[0] :
			lista.insert( 0 , lista[1] )
			lista.pop(2)
	c += 1

print(lista)
