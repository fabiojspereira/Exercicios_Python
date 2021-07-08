def menu_adaptavel ( txt ):
	tamanho = len(txt) + 6
	print(f"{'*' * tamanho}")
	print(f"   {txt}")
	print(f"{'*' * tamanho}")


# Programa Principal
mensagem = str(input("Digite a mensagem a ser exibida no menu adaptável : ")).strip()

menu_adaptavel(mensagem)
menu_adaptavel("Fabio Jorge de Souza Pereira")
