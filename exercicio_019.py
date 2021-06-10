from random import choice

import random
aluno_01 = str(input("Digite o nome do primeiro aluno que concorre ao sorteio : "))
aluno_02 = str(input("Digite o nome do segundo aluno que concorre ao sorteio : "))
aluno_03 = str(input("Digite o nome do terceiro aluno que concorre ao sorteio : "))
aluno_04 = str(input("Digite o nome do quarto aluno que concorre ao sorteio : "))

lista = [aluno_01, aluno_02, aluno_03, aluno_04]

#print ("O aluno escolhido no sorteio foi : {}. Parabéns !".format(random.choice([aluno_01, aluno_02, aluno_03, aluno_04])))

print ("O aluno escolhido no sorteio foi : {}. Parabéns !".format(choice(lista)))