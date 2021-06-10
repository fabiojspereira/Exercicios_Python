primeiro_t = int(input("\nDigite o primeiro termo da P.A. : "))
razao = int(input("Digite a razão da P.A. : "))

print('''
Fórmula da P.A. : 
PA = (a, a + r, a + 2r) onde a = primeiro_t // a + 1r = segundo termo // a + 2r = terceiro termo
						onde r = razão
						
N-ézimo termo : an = a1 + (n – 1) . r
''')


print("\nVamos calcular uma P.A. com 10 termos :")

for count in range (1,11,1):
	print("{:2}º Termo : {:3}.".format(count, (primeiro_t + ((count - 1) * razao))))


print("\nFim.")

'''
for count in range (1,11):
	if count == 1:
		print("{}º Termo : {}.".format(count, primeiro_t))
	elif count == 2:
		print("{}º Termo : {}.".format(count, ( primeiro_t + ((count-1) * razao))))
	else:
		print("{}º Termo : {}.".format(count, ( primeiro_t + ((count - 1) * razao))))
'''