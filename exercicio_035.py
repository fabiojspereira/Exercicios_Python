print("*-" * 22)
print("Vamos testar a existência de um triângulo !")
print("*-" * 22)

reta_01 = float(input("\nDigite o tamanho da reta 01 : "))
reta_02 = float(input("Digite o tamanho da reta 02 : "))
reta_03 = float(input("Digite o tamanho da reta 03 : "))

if (reta_02 - reta_03) < reta_01 < (reta_02 + reta_03) and (reta_01 - reta_03) < reta_02 < (reta_01 + reta_03) and (reta_01 - reta_02) < reta_03 < (reta_01 + reta_02):
    print("\nCom estas medidas {}, {} e {}, é possível que exista um triângulo.".format(reta_01, reta_02, reta_03))
else:
    print("\nCom estas medidas {}, {} e {}, não é possível que venha a existir um triângulo.".format(reta_01, reta_02, reta_03))
