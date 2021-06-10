print("Vamos exibir a tabuada completa ! Defina um número inteiro : ")
numero = int(input("Número : "))

print("\nTABUADA do {}".format(numero))
for count in range (1,11):
	print("{} x {:2} = {:2}".format(numero,count,numero*count))

print("Fim.")
