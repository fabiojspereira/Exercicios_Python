print("Vamos calcular o aumento salarial do funcionário.")
funcionario = str(input("Digite o valor do funcionário : "))
salario_base = float(input("Digite o valor do salário atual do funcionário chamado {} : ".format(funcionario)))

print("O funcionário {} que tem o salário atual de R$ {:.2f}\nPassa a ter seu salário corrigido para R$ {:.2f}.".format(funcionario,salario_base,salario_base+((salario_base*15)/100)))
print("O aumento real do salário foi de 15%, ou seja, R$ {:.2f}.".format((salario_base*15)/100))

#salario_base+((salario_base*15)/100)
