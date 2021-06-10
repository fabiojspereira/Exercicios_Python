print("\nDigite seis valores inteiros para que eu faça a soma apenas dos números pares")
count = 0
soma = 0
palavra = ""
for c in range(1,7):

	numero = int(input("Digite o {}º número : ".format(c)))
	if numero % 2 == 0:
		soma = soma + numero
		count = count + 1

if count == 0:
	print("\nNão foram informados números pares...")
elif count == 1:
	print("Foi informado apenas um número par. A soma é {}.".format(soma))
else:
	print("foram informados {} números pares e a soma deles é {}".format(count,soma))

