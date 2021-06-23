primeiro_t = int(input("\nDigite o primeiro termo da P.A. : "))
razao = int(input("Digite a razão da P.A. : "))

print("\nVamos calcular uma P.A. com 10 termos :")

geral = 1
count_01 = 1
esc_01 = 1

while esc_01 != 0:
	while count_01 < 11:
		print("{:2}º Termo : {:3}.".format(count_01, (primeiro_t + ((count_01 - 1) * razao))))
		count_01 = count_01 + 1
		geral = geral + 1

	print("\nDeseja calcular mais quantos termos desta P.A ?")
	esc_01 = int(input(": "))
	count_02 = 1
	while count_02 <= esc_01:
		print("{:2}º Termo : {:3}.".format(geral, (primeiro_t + ((geral - 1) * razao))))
		count_02 = count_02 + 1
		geral = geral + 1

print("Total de termos : {}.".format(geral - 1))
print("\nFinalizando")

'''
primeiro_t = int(input("\nDigite o primeiro termo da P.A. : "))
razao = int(input("Digite a razão da P.A. : "))

print("\nVamos calcular uma P.A. com 10 termos :")

geral = 1
count_01 = 1
esc_01 = 1

while esc_01 != 0:
	while count_01 < 11:
		print("{:2}º Termo : {:3}.".format(count_01, (primeiro_t + ((count_01 - 1) * razao))))
		count_01 = count_01 + 1
		geral = geral + 1
		# print(count)

	print("\nDeseja calcular mais quantos termos desta P.A ?")
	esc_01 = int(input(": "))
	#if esc_01 == 0:
	#	esc_01 = 0
	else:
		count_02 = 0
		while count_02 < esc_01:
			print("{:2}º Termo : {:3}.".format(geral, (primeiro_t + ((geral - 1) * razao))))
			#count_02 = count_02 + 1
			geral = geral + 1

print("Total de termos : {}.".format(geral))
print("\nFinalizando")
'''
