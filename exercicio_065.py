esc_01 = "sim"
soma = 0
contador = 0

manior = 0
menor = 0

#lista_negativa = ["não", "nao", "n"]

while esc_01 != "não" and esc_01 != "nao" and esc_01 != "n":
	numero = int(input("Digite um número inteiro : "))
	print("Deseja digitar outro número ? [ sim / não ]", end="")
	esc_01 = str(input(": ")).strip().lower()[0:3]
	soma = soma + numero
	contador = contador + 1
	if contador == 1:
		maior = numero
		menor = numero

	if numero > maior:
		maior = numero
	if numero < menor:
		menor = numero

print("\nQuantidade de números digitados : {}.".format(contador))
print("Média entre os {} números : {:.2f}.".format(contador, soma / contador))
print("O maior número digitado foi o número {} e o menor foi {}".format(maior,menor))
print('\nPrograma finalizado.')
#while esc_01 == "sim" or esc_01 == "s":
#while esc_01 != lista_negativa[0] and esc_01 != lista_negativa[1] and esc_01 != lista_negativa[2]:

