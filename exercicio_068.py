from random import randint

x = len("Jogo do PAR ou ÍMPAR")
print("*" * x)
print("Jogo do PAR ou ÍMPAR")
print("*" * x)

vencer = True
conta_vitoria = 0
soma = 0

while vencer == True:

	n_h = int(input("\nDigite o seu valor de 0 a 10 : "))  # Escolha do número humano.
	n_m = randint(0, 10)  # Escolha do número da máquina.
	soma = n_h + n_m

	if soma % 2 == 0:
		p_ou_i = "par"
	else:
		p_ou_i = "ímpar"

	if 10 >= n_h >= 0:
		p_i_h = str(input("\nVocê deseja escolher PAR ou ÍMPAR ? [ P / I ] : ")).strip().lower()[:1] # Escolha PAR ou ÍMPAR humano.

		if p_i_h == "p":
			p_i_h = "par"
			p_i_m = "ímpar"
		elif p_i_h == "i" or p_i_h == "í":
			p_i_h = "ímpar"
			p_i_m = "par"
		else:
				print("Você não digitou uma opção válida para par ou ímpar ...")

		if p_i_h == p_ou_i:
			vencer = True
			conta_vitoria = conta_vitoria + 1
			print(f"Você escolheu o número {n_h} e o computador escolheu o número {n_m}. O total é {soma}. Deu {p_ou_i} !")
			print("\033[1;32mVocê venceu ! Continue jogando !\033[m")
		else:
			vencer = False
			print(f"Você escolheu o número {n_h} e o computador escolheu o número {n_m}. O total é {soma}. Deu {p_ou_i} !")
			print("\033[1;31mVocê perdeu ! GAME OVER !!!\033[m")
			print("\033[1;33mVocê venceu {} vezes!\033[m".format(conta_vitoria))

	else:
		print("\033[1;31mVocê digitou um número fora do interválo de 0 a 10... Tente novamente...\033[m ")
