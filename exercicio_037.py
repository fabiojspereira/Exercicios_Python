numero = int(input("Digite um número inteiro para ser convertido : "))

print("1 - converter para binário")
print("2 - converter para octadecimal")
print("3 - converter para hexadecimal")
escolha = int(input(": "))

if escolha == 1:
	print("O número inteiro {} convertido para binário é : {}".format(numero, bin(numero)[2:]))
elif escolha == 2:
	print("O número inteiro {} convertido para octadecimal é : {}".format(numero, oct(numero)[2:]))
elif escolha == 3:
	print("O número inteiro {} convertido para hexadecimal é : {}".format(numero, hex(numero)[2:]))
else:
	print("opção inválida.")
