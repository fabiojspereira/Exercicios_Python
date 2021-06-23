qtd = 0
soma = 0

numero = int(input("Digite um número inteiro : "))
while numero != 999:
	soma = soma + numero
	qtd = qtd + 1
	numero = int(input("Digite um número inteiro : "))

print("\nQuantidade de números digitados : {}.".format(qtd))
print("* desconsiderando o 999 para sair.")
print("\nA soma entre todos os números é : {}".format(soma))
print("Fim.")
