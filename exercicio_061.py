primeiro_t = int(input("\nDigite o primeiro termo da P.A. : "))
razao = int(input("Digite a razão da P.A. : "))

print("\nVamos calcular uma P.A. com 10 termos :")

count = 1
while count < 11:

	print("{:2}º Termo : {:>3}.".format(count, (primeiro_t + ((count - 1) * razao))))
	count = count + 1
print("\nFim.")
# for count in range ( 1, 11, 1 ): Caso queira fazer com for.


'''
Fórmula da P.A. : 
PA = (a, a + r, a + 2r) onde a = primeiro_t // a + 1r = segundo termo // a + 2r = terceiro termo
						onde r = razão

N-ézimo termo : an = a1 + (n – 1) . r
'''


