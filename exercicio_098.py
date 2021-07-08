from time import sleep


def contador( inicio, fim, passo ):

	if passo < 0 :
		passo = passo * -1
	if passo == 0 :
		passo = 1

	print(f"\nContagem de {inicio} até {fim} de {passo} em {passo} : ")
	sleep(1)

	if inicio < fim :
		numero = inicio
		while numero <= fim :
			print(f"\033[1;34m{numero}\033[m",end=" ")
			sleep(0.25)
			numero = numero + passo
		print("\033[1;35m- FIM\033[m")

	if inicio > fim :
		numero = inicio
		while numero >= fim :
			print(f"\033[1;34m{numero}\033[m",end=" ")
			sleep(0.25)
			numero = numero - passo
		print("\033[1;35m- FIM\033[m")


# Programa Principal
contador( 1, 10, 1 )
contador( 10, 0, 2 )

print("\nAgora é sua vez de escolher os parâmetros :")
inicio = int(input(f"{'Início':<8}{': ':>10}"))
fim = int(input(f"{'Fim':<8}{': ':>10}"))
passo = int(input(f"{'Passo':<8}{': ':>10}"))
contador( inicio, fim, passo )
