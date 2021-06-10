import random

aluno_01 = str(input("Digite o nome do primeiro aluno do grupo : "))
aluno_02 = str(input("Digite o nome do segundo aluno do grupo : "))
aluno_03 = str(input("Digite o nome do terceiro aluno do grupo : "))
aluno_04 = str(input("Digite o nome do quarto aluno do grupo : "))

lista = [aluno_01, aluno_02, aluno_03, aluno_04]

random.shuffle(lista)
print ("Lista sorteada {}".format(lista))


#random.shuffle([aluno_01, aluno_02, aluno_03, aluno_04])