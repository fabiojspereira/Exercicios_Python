print("Vamos calcular a área de uma parede e também a quantidade de tinta necessária para pintá-la.")
largura = float(input("Digite o valor da largura em metros(m) da parede : "))
altura = float(input("Digite o valor da altura em metros(m) da parede : "))
area_parede = (largura*altura)

print("A área da sua parede é de {:.3f} m2.".format(area_parede))

print("Cala litro(l) de tinta pinta 2 metros quadrados (m2)")
print ("A sua parede tem {:.3f} m2 de área útil. Será necessário {:.4f} litros de tinta para pintá-la.".format(area_parede,(area_parede/2)))
