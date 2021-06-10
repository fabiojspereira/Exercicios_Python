maior_peso = 0
menor_peso = 0

for pessoa in range (0, 5):
	peso = float(input("Digite o peso da {}º pessoa : ".format(pessoa + 1 )))
	if pessoa == 0:
		maior_peso = peso
		menor_peso = peso
	else:
		if peso > maior_peso:
			maior_peso = peso
		if peso < menor_peso:
			menor_peso = peso

print("\nA pessoa mais pesada tem : {:.1f} kgs".format(maior_peso))
print("A pessoa mais leve tem : {:.1f} kgs ".format(menor_peso))


'''
maior_peso = 0
menor_peso = 1000

for pessoa in range (0, 5):
	peso = float(input("Digite o peso da {}º pessoa : ".format(pessoa + 1 )))

	if peso >= maior_peso:
		maior_peso = peso
	if peso <= menor_peso:
		menor_peso = peso

print("\nA pessoa mais pesada tem : 	{:.1f} kgs".format(maior_peso))
print("A pessoa mais leve tem : {:.1f} kgs ".format(menor_peso))
'''