print("Programa que calcula a soma entre todos os números ímpares, múltiplos de 3 entre 1 e 500")

contador = 0
soma = 0
lista = [] # Aqui a lista é criada vazia

for numero in range(1, 51):
	if numero % 2 == 1 and numero % 3 == 0:
		soma = soma + numero
		lista = lista + [numero] # Aqui a lista recebe o item
		#lista.append(count)  # Aqui a lista recebe o item
		contador = contador + 1
		print("\nNúmero = {}\nSoma = {}".format(numero, soma))

print("\n")
print("Quantidade de números elegíveis : {}.".format(contador))

print("LISTA : {}".format(lista))

'''
print(lista[0:5]) # O índice final nunca entra na contagem por isso tem que repetir na sequência de baixo
print(lista[5:10])
print(lista[10:15])
print(lista[15:20])
print(lista[20:25])
print(lista[25:30])
print(lista[30:35])
print(lista[35:40])
print(lista[40:45])
print(lista[45:50])
print(lista[50:55])
print(lista[55:60])
print(lista[60:65])
print(lista[65:70])
print(lista[70:75])
print(lista[75:80])
print(lista[80:85])
print(lista[85:90])
print(lista[90:95])
print(lista[95:100])
'''
