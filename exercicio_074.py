from random import randint

print("Vou gerar 5 números aleatórios : ")
tupla = (randint(0, 10)), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
#				   0				1				2				3				4
print(f"\nTupla : {tupla}", end="")
maior = menor = tupla[0]

for count in range( 0 , len(tupla) ):
	if tupla[count] > maior:
		maior = tupla[count]
	if tupla[count] < menor:
		menor = tupla[count]

print(f"\nMaior Valor : {maior}")
print(f"Menor Valor : {menor}")

# Ou usar o método que tem dentro das tuplas, o max().
print("\nUtilizando max() :")
print(f"O maior valor sorteado foi {max(tupla)}")
print(f"O menor valor sorteado foi {min(tupla)}")

'''
tupla1 = tupla2 = tupla3 = tupla4 = tupla5 = ()

print("Vou gerar 5 números aleatórios : ")
tupla1 = randint(0, 10)
print(tupla1,end=" ")
maior = tupla1
menor = tupla1

tupla2 = randint(0, 10)
print(tupla2,end=" ")
if tupla2 > maior:
	maior = tupla2
if tupla2 < menor:
	menor = tupla2

tupla3 = randint(0, 10)
print(tupla3,end=" ")
if tupla3 > maior:
	maior = tupla3
if tupla3 < menor:
	menor = tupla3

tupla4 = randint(0, 10)
print(tupla4,end=" ")
if tupla4 > maior:
	maior = tupla4
if tupla4 < menor:
	menor = tupla4

tupla5 = randint(0, 10)
print(tupla5)
if tupla5 > maior:
	maior = tupla5
if tupla5 < menor:
	menor = tupla5

tupla = tupla1, tupla2, tupla3, tupla4, tupla5

print("\nTupla : ", end="")
print(tupla)

print(f"\nMaior Valor : {maior}")
print(f"Menor Valor : {menor}")
'''
