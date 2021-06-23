print("\033[0;30;47m*\033[m" * 40)
# print("\033[0;30;46m{:^40}\033[m".format("*"))
print("\033[1;30;43m{:^40}\033[m".format("BANCO FJSP"))
# print("\033[0;30;46m{:^40}\033[m".format("*"))
print("\033[0;30;47m*\033[m" * 40)
print("\n>>>> Digite o valor do saque <<<<")
print("Cédulas disponíveis : 200,100,50,20,10,5,1")
valor = int(input("\nR$ "))

nota = 200
qtd_nota = 0

controle_01 = True
while controle_01 == True :
	if valor >= nota : #151 #51
		valor = valor - nota # valor = 151 = 51 = 1
		qtd_nota = qtd_nota + 1 #1
	else:
		if qtd_nota > 0:
			print(f"Total de {qtd_nota} notas de R$ {nota}.")
			qtd_nota = 0
		if nota == 200 :
			nota = 100
		elif nota == 100 :
			nota = 50
		elif nota == 50 :
			nota = 20
		elif nota == 20 :
			nota = 10
		elif nota == 10 :
			nota = 5
		elif nota == 5 :
			nota = 1
		#qtd_nota = 0
		if valor == 0 :
			controle_01 = False
print ("FIM")

'''
print("\033[0;30;47m*\033[m" * 40)
# print("\033[0;30;46m{:^40}\033[m".format("*"))
print("\033[1;30;43m{:^40}\033[m".format("BANCO FJSP"))
# print("\033[0;30;46m{:^40}\033[m".format("*"))
print("\033[0;30;47m*\033[m" * 40)

print("\n>>>> Digite o valor do saque <<<<")
print("Cédulas disponíveis : 100,50,20,10,1")
valor = int(input("\nR$ "))

novo_valor = 0

qtd_nota_200 = qtd_nota_100 = qtd_nota_50 = qtd_nota_20 = qtd_nota_10 = qtd_nota_05 = qtd_nota_01 = 0

controle_01 = False
while controle_01 == False:
# INÍCIO DO TRATAMENTO DE NOTAS DE 100
	if valor // 100 > 0:										# 100
		qtd_nota_100 = valor // 100
		valor = valor - ( qtd_nota_100 * 100 )
		if valor == 0:
			break

		if valor // 50 > 0:  									# 150
			qtd_nota_50 = valor // 50  							#
			valor = valor - ( qtd_nota_50 * 50 ) 				#
			if valor == 0:
				break

			if valor // 20 > 0:  								# 170
				qtd_nota_20 = valor // 20  						#
				valor = valor - ( qtd_nota_20 * 20 )  			#
				if valor == 0:
					break

				if valor // 10 > 0:  							# 180
					qtd_nota_10 = valor // 10  					#
					valor = valor - ( qtd_nota_10 * 10 )  		#
					if valor == 0:
						break

					if valor // 1 > 0:							# 181
						qtd_nota_01 = valor // 1  				#
						valor = valor - ( qtd_nota_01 * 1 ) 	#
						controle_01 = True

				elif valor // 1 > 0: 							# 171
					qtd_nota_01 = valor // 1  					#
					valor = valor - ( qtd_nota_01 * 1 )  		#
					controle_01 = True

			elif valor // 10 > 0:  								# 160
				qtd_nota_10 = valor // 10  						#
				valor = valor - ( qtd_nota_10 * 10 )  			#
				if valor == 0:
					break

				if valor // 1 > 0:  							# 161
					qtd_nota_01 = valor // 1  					#
					valor = valor - ( qtd_nota_01 * 1 )  		#
					controle_01 = True

			elif valor // 1 > 0:  								# 151
				qtd_nota_01 = valor // 1  						#
				valor = valor - ( qtd_nota_01 * 1 )  			#
				controle_01 = True
# FIM DO TRATAMENTO DE NOTAS DE 100

# INÍCIO DO TRATAMENTO DE NOTAS DE 50
	if valor // 50 > 0:  										# 50
		qtd_nota_50 = valor // 50  								#
		valor = valor - ( qtd_nota_50 * 50 ) 					#
		if valor == 0:
			break

		if valor // 20 > 0:  									# 70
			qtd_nota_20 = valor // 20  							#
			valor = valor - ( qtd_nota_20 * 20 )  				#
			if valor == 0:
				break

			if valor // 10 > 0:  								# 80
				qtd_nota_10 = valor // 10  						#
				valor = valor - ( qtd_nota_10 * 10 )  			#
				if valor == 0:
					break

				if valor // 1 > 0:								# 81
					qtd_nota_01 = valor // 1  					#
					valor = valor - ( qtd_nota_01 * 1 ) 		#
					controle_01 = True

			elif valor // 1 > 0: 								# 71
				qtd_nota_01 = valor // 1  						#
				valor = valor - ( qtd_nota_01 * 1 )  			#
				controle_01 = True

		elif valor // 10 > 0:  									# 60
			qtd_nota_10 = valor // 10  							#
			valor = valor - ( qtd_nota_10 * 10 )  				#
			if valor == 0:
				break

			if valor // 1 > 0:  								# 61
				qtd_nota_01 = valor // 1  						#
				valor = valor - ( qtd_nota_01 * 1 )  			#
				controle_01 = True

		elif valor // 1 > 0:  									# 51
			qtd_nota_01 = valor // 1  							#
			valor = valor - ( qtd_nota_01 * 1 )  				#
			controle_01 = True
# FIM DO TRATAMENTO DE NOTAS DE 50

# INÍCIO DO TRATAMENTO DE NOTAS DE 20
	if valor // 20 > 0:  										# 20
		qtd_nota_20 = valor // 20  								#
		valor = valor - ( qtd_nota_20 * 20 )  					#
		if valor == 0:
			break

		if valor // 10 > 0:  									# 30
			qtd_nota_10 = valor // 10  							#
			valor = valor - ( qtd_nota_10 * 10 )  				#
			if valor == 0:
				break

			if valor // 1 > 0:									# 31
				qtd_nota_01 = valor // 1  						#
				valor = valor - ( qtd_nota_01 * 1 )  			#
				controle_01 = True

		elif valor // 1 > 0: 									# 21
			qtd_nota_01 = valor // 1  							#
			valor = valor - ( qtd_nota_01 * 1 )  				#
			controle_01 = True
# FIM DO TRATAMENTO DE NOTAS DE 20

# INÍCIO DO TRATAMENTO DE NOTAS DE 10
	if valor // 10 > 0:  										# 10
		qtd_nota_10 = valor // 10  								#
		valor = valor - ( qtd_nota_10 * 10 )  					#
		if valor == 0:
			break

		if valor // 1 > 0:										# 11
			qtd_nota_01 = valor // 1  							#
			valor = valor - ( qtd_nota_01 * 1 )  				#
			controle_01 = True
# FIM DO TRATAMENTO DE NOTAS DE 10

# INÍCIO DO TRATAMENTO DE NOTAS DE 1
	if valor // 1 > 0:											# 1
		qtd_nota_01 = valor // 1  								#
		valor = valor - ( qtd_nota_01 * 1 )  					#
		controle_01 = True
# FIM DO TRATAMENTO DE NOTAS DE 1

print(f"\nCédulas de R$ 100,00 : {qtd_nota_100}")
print(f"\nCédulas de R$ 50,00 : {qtd_nota_50}")
print(f"\nCédulas de R$ 20,00 : {qtd_nota_20}")
print(f"\nCédulas de R$ 10,00 : {qtd_nota_10}")
print(f"\nCédulas de R$ 1,00 : {qtd_nota_01}")

'''
