salario = float(input("Digite o valor do salário do funcionário atualmente : "))
print ("\nCom base no valor do salário do funcionário, iremos calcular o aumento corresponente.")

if salario > 1250 :
    aumento = salario * 10 / 100
    novo_salario = salario + aumento
    print("\nO aumento salarial foi de 10%. Isso equivale a R$ {:.2f}. O seu salário agora é de : R$ {:.2f}.".format(aumento,novo_salario))

if salario <= 1250 :
    aumento = salario * 15 / 100
    novo_salario = salario + aumento
    print("\nO aumento salarial foi de 15%. Isso Equivale a R$ {:.2f}. O seu salário agora é de : R$ {:.2f}.".format(aumento,novo_salario))
