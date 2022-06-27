n = 0
soma = 0
count = 0

while n != 999:
	n = int(input("Digite um número inteiro *999 para sair : "))
	if n == 999:
		break
	count += + 1
	soma = soma + n

print(f"A soma de todos os {count} números é : {soma}")
