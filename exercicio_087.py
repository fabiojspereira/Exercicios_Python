matrix_load = [ [], [], [], [], [], [], [], [], [] ]
#				 1   2   3   4   5   6   7   8   9
soma_terceira_coluna = pares_soma = count = 0

for linha in range ( 0, 3 ) :
	for coluna in range ( 0 , 3 ) :
		n = int(input(f"Digite o valor para [{linha},{coluna}] : "))
		matrix_load[count].append(n)
		count += 1

		if n % 2 == 0 :
			pares_soma = pares_soma + n

		if coluna == 2 :
			soma_terceira_coluna = soma_terceira_coluna + n

		if linha == 1 and coluna == 0 :
			maior_valor_segunda = n
		elif linha == 1 and coluna >= 1 :
			if n > maior_valor_segunda :
				maior_valor_segunda = n

print(matrix_load[0:3])
print(matrix_load[3:6])
print(matrix_load[6:9])

print(f"\nA soma dos números pares é : {pares_soma}.")
print(f"A soma dos valores da terceira coluna é : {soma_terceira_coluna}.")
print(f"O maior valor da segunda linha é : {maior_valor_segunda}.")
