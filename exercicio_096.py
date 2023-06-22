def area(L, C):
	calc_area = (L * C)
	print(f"A área do terreno com largura {L:.2f}m e comprimento {C:.2f}m é {calc_area}m².")


def linha():
	print("*" * 40)


# Programa Principal
linha()
print(f"{'Calculadora de área para terrenos':^40}")
linha()

L = float(input("\nDigite a largura do terreno em metros     : "))
C = float(input("Digite o comprimento do terreno em metros : "))
print()

linha()
area(L, C)
