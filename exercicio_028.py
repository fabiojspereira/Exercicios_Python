from random import choice
from time import sleep

print("*-"*34)
print("O computador vai pensar em um número entre 0 e 5. Tente acertar !!!")
print("*-"*34)

lista = [1,2,3,4,5,]
#npc = random.choice(lista)
npc = choice(lista)

print("Escolhendo número. Aguarde...Pronto ! Agora tente desvendar !\n")
sleep(1)
nh = int(input("Digite o seu número e vamos ver se você acertou : "))

if npc == nh:
    print("Nossa ! Você acertou ! Eu escolhi o número {} também.".format(npc))
else:
    print("Ahhhh você errou... Eu tinha escolhido o número {} e não o número {}.".format(npc,nh))
