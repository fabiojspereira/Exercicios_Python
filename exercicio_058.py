from random import choice
from random import shuffle
from time import sleep

x = len("O computador vai pensar em um número entre 0 e 10. Tente adivinhar !!!")
print("\033[1;34m*\033[m" * x)
print("O computador vai pensar em um número entre 0 e 10. Tente adivinhar !!!")
print("\033[1;34m*\033[m" * x)

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(lista)  # Para dificultar...
# print(lista)
sleep(0.5)
print("\nO computador está escolhendo um número. Aguarde... \nPronto ! Agora tente desvendar !\n")
npc = choice(lista)  # Aqui é a escolha do computador

tentativa = 0

acerto = "error"
while acerto != "ok":
	nh = int(input("Digite o seu número e vamos ver se você irá acertar : "))
	if npc == nh:
		print("\033[1;32m\nNossa ! Você acertou ! Eu escolhi o número {} também.\033[m".format(npc))
		tentativa = tentativa + 1
		acerto = "ok"
	else:
		print("\033[1;31mAhhhh você errou... Tente novamente.\033[m")
		tentativa = tentativa + 1
		acerto = "error"
if tentativa == 1:
	print("\033[1;32mVocê acertou de primeira !!!\033[m")
else:
	print("Você precisou de {} tentativas para acertar !".format(tentativa))
print("\033[1;33m\nO jogo chegou ao fim.\033[m")
