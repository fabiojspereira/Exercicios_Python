from time import sleep
print("\nDigite dois números e serão exibidas as operações disponíveis.")
n1 = float(input("Digite o primeiro número : "))
n2 = float(input("Digite o segundo número : "))
controle = 0

while controle != 5:

	print("\nMENU DE OPERAÇÕES : ")
	print("\033[1;32m[1]\033[m - Somar os números")
	print("\033[1;32m[2]\033[m - Multiplicar os números")
	print("\033[1;32m[3]\033[m - Exibir o maior número")
	print("\033[1;32m[4]\033[m - Digitar novos números")
	print("\033[1;31m[5]\033[m - Sair do programa")
	esc_1 = int(input(": "))

	if esc_1 == 1:
		soma = n1 + n2
		print("\033[1;32m\n[1]\033[m - Somar os números")
		print("A soma dos números \033[1;34m{}\033[m e \033[1;34m{}\033[m é igual a : \033[1;37m{}\033[m.".format(n1, n2, soma))
		controle = 1

	elif esc_1 == 2:
		multiplica = n1 * n2
		print("\033[1;32m\n[2]\033[m - Multiplicar os números")
		print("A multiplicação dos números \033[1;34m{}\033[m e \033[1;34m{}\033[m é igual a : \033[1;37m{}\033[m.".format(n1, n2, multiplica))
		controle = 2

	elif esc_1 == 3:
		print("\033[1;32m\n[3]\033[m - Exibir o maior número")
		if n1 > n2:
			print("O número \033[1;34m{}\033[m é maior que o número \033[1;34m{}\033[m.".format(n1, n2))
		else:
			print("O número \033[1;34m{}\033[m é maior que o número \033[1;34m{}\033[m.".format(n2, n1))
		controle = 3

	elif esc_1 == 4:
		print("\nDigite dois números e serão exibidas as operações disponíveis.")
		n1 = float(input("Digite o primeiro número : "))
		n2 = float(input("Digite o segundo número : "))
		controle = 4

	elif esc_1 == 5:
		controle = 5

	else:
		print("Opção inválida !")
		controle = 0
	sleep(2) # Faz o MENU ter um atraso.
print("\nSaindo do programa ...")
