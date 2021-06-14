from math import hypot

cateto_oposto = float(input("Digite o valor do cateto oposto do triângulo retângulo : "))
cateto_adj = float(input("Digite o valor do cateto adjacente do triângulo retângulo : "))

print ("A hipotenusa deste triângulo é {:.2f} ".format( hypot(cateto_oposto,cateto_adj)))
