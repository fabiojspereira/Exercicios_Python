print("Digite a quantidade de itens a serem exibidos na sequência de Fibonacci : ")
n = int(input(": "))

f0 = 0
f1 = 1

print("{}".format(f0), end=" -> ")
print("{}".format(f1), end=" -> ")
contador = 1
while contador != n - 1:
	print("{}".format(f0 + f1), end="")
	print(" -> " if contador < n - 2 else " : ", end="")
	soma = (f0 + f1)
	f0 = f1
	f1 = soma
	contador = contador + 1
print("\nIterações : {}.".format(n))
print("\n\nFim.")
# for count_01 in range(1, n - 1): Caso queira fazer com for.
