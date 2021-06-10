n = int(input("Digite um número para o cálculo do fatorial[n!] : "))
x = n
t = n
fatorial = 1

while x != 1 and x != 0:
	t = x * (x - 1)
	x = x - 2
	fatorial = fatorial * t

print(fatorial)
print("O fatorial de {}, representado por {}! é {}.".format(n, n, fatorial))
