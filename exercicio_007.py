#print ("Vamos calcular a média aritimética do aluno.")
aluno = str(input("Vamos calcular a média aritimética do aluno.\nDigite o nome do aluno : "))
n1 = float(input("Digite a primeira nota do aluno chamado {:10} : ".format(aluno)))
n2 = float(input("Digite a segunda nota do aluno chamado {:11} : ".format(aluno)))
print ("Calculando a média aritimética ...")
print ("A média foi calculada : {:.3f}".format((n1+n2)/2))

