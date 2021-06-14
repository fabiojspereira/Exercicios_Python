import random
import time
import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("som.mp3")
pygame.mixer.music.play()

x = len("PEDRA - PAPEL - TESOURA")
print("\033[1;32m*\033[m" * x)
print("\033[1;33mPEDRA\033[m - \033[1;34mPAPEL\033[m - \033[1;35mTESOURA\033[m")
print("\033[1;32m*\033[m" * x)

print("\nVamos brincar de pedra, papel e tesoura !!!")
print('''\033[4;37m\nREGRAS\033[m : 
\nO papel ganha da pedra porque a embrulha.
A tesoura ganha do papel porque o corta.
A pedra, por sua vez, ganha da tesoura porque a quebra.''')

wait = input("\n\033[37mAperte [enter] para iniciar o jogo ...\033[m")

print('''\nEscolha a sua jogada :
\033[32m1 para Pedra.
2 para Papel.
3 para Tesoura.\033[m''')
h_escolha = int(input(": "))

lista = ["Pedra", "Papel", "Tesoura"]
#random.shuffle(lista)
print("\nO computador está fazendo a sua escolha ... ")
time.sleep(1)
m_escolha = random.choice(lista)

if h_escolha != 1 and h_escolha != 2 and h_escolha != 3 and h_escolha != 4:
	print("\033[1;31m\nVocê não escolheu uma opção válida !!!\033[m")

if h_escolha == 1:
	if m_escolha == lista[0]:
		print("\n\033[1;37mDeu empate ! Todos escolheram a Pedra !\033[m")
		print("\033[37mHumano escolheu {} e o Computador escolheu {}.\033[m".format(lista[0],m_escolha))
	elif m_escolha == lista[1]:
		print("\n\033[1;33mO Papel embrulha a Pedra ! O computador ganhou !\033[m")
		print("\033[37mHumano escolheu {} e o Computador escolheu {}.\033[m".format(lista[0],m_escolha))
	elif m_escolha == lista[2]:
		print("\n\033[1;32mA Pedra quebra a Tesoura ! Você venceu !\033[m")
		print("\033[37mHumano escolheu {} e o Computador escolheu {}.\033[m".format(lista[0],m_escolha))

if h_escolha == 2:
	if m_escolha == lista[0]:
		print("\n\033[1;32mO Papel embrulha a Pedra ! Você venceu !\033[m")
		print("\033[37mHumano escolheu {} e o Computador escolheu {}.\033[m".format(lista[1], m_escolha))
	elif m_escolha == lista[1]:
		print("\n\033[1;37mDeu empate ! Todos escolheram o papel !\033[m")
		print("\033[37mHumano escolheu {} e o Computador escolheu {}.\033[m".format(lista[1], m_escolha))
	elif m_escolha == lista[2]:
		print("\n\033[1;33mA Tesoura corta o Papel ! O computador ganhou !\033[m")
		print("\033[37mHumano escolheu {} e o Computador escolheu {}.\033[m".format(lista[1], m_escolha))

if h_escolha == 3:
	if m_escolha == lista[0]:
		print("\n\033[1;33mA Pedra quebra a Tesoura ! O computador ganhou !\033[m")
		print("\033[37mHumano escolheu {} e o Computador escolheu {}.\033[m".format(lista[2], m_escolha))
	elif m_escolha == lista[1]:
		print("\n\033[1;32mA Tesoura corta o Papel ! Você venceu !\033[m")
		print("\033[37mHumano escolheu {} e o Computador escolheu {}.\033[m".format(lista[2], m_escolha))
	elif m_escolha == lista[2]:
		print("\n\033[1;37mDeu empate ! Todos escolheram a Tesoura !\033[m")
		print("\033[37mHumano escolheu {} e o Computador escolheu {}.\033[m".format(lista[2], m_escolha))

wait = input("\n\033[37mAperte [enter] para finalizar o jogo ...\033[m")
