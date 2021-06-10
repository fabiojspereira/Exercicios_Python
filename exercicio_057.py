check = ""

while check != "ok":
	sexo = str(input("Digite o sexo da pessoa [ M / F ] : ")).strip().lower()
	if sexo == "m" or sexo == "f":
		check = "ok"
	else:
		check = "error"
		print("Opção inválida ! Tente novamente.")
print("\nDigitação OK. Fim.")

'''
sexo = str(input("Digite o sexo da pessoa [ M / F ] : ")).strip().lower()[0]

while sexo not in "MmFf":
	print("Opção inválida ! Tente novamente.")
	sexo = str(input("Digite o sexo da pessoa [ M / F ] : ")).strip().lower()[0]

print("Digitação OK. Fim.")
'''