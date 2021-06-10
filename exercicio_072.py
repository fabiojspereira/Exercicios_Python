extenso = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","catorze",
		   "quinze","dezesseis","dezessete","dezoito","dezenove","vinte")

#print(len(extenso))

continua = True
while continua == True :
	numero = int(input("Digite um número entre 0 e 20 : "))
	if 0 <= numero <= 20 :
		print(f"Você digitou o número {extenso[numero]}")
		esc_01 = str(input("Deseja continuar [ sim / Não ] ? ")).strip().lower()[0]
		if esc_01 == "s":
			continua = True
		else:
			continua = False
	else:
		print("Valor incorreto !")
		continua = True

print("FIM")

