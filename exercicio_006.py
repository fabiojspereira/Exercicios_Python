num1 = int(input(" Digite um número e irei calcular o dobro, o triplo e a raiz quadrada :"))

print ("O dobro do número {: >20} é :".format(num1), (num1*2))
print ("O triplo do número {: >19} é :".format(num1), (num1*3))
print ("A raiz quadradda do número {: >11} é : {:.3f}".format(num1, (num1**(1/2))))

# linha única
# print ("O dobro do número {: >20} é :".format(num1),(num1*2),"\nO triplo do número {: >19} é :".format(num1),(num1*3),"\nA raiz quadradda do número {: 11} é :".format(num1),(num1**(1/2)))
