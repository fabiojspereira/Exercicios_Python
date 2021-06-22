lista_numeros = [ [], [] ]

for count in range ( 0, 7 ) :
	n = int(input(f"Digite o {count+1}º número : "))
	if n % 2 == 0 :
		lista_numeros[0].append(n)
	else :
		lista_numeros[1].append(n)

lista_numeros[0].sort()
lista_numeros[1].sort()
print(f"\nLista de números pares : {lista_numeros[0]}")
print(f"Lista de números ímpares : {lista_numeros[1]}")
