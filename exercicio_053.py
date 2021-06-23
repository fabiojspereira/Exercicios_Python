frase = str(input("Digite uma frase e irei verificar se ela é um palíndromo : ")).strip().upper()

palavra = frase.split()  # Divide a frase em palavras e joga na lista.
print("\nPalavras separadas {}".format(palavra))
# print(palavra[0],palavra[1]) # imprime na tela a palavra com índice 0 e a palavra com índice 1.

qtd_palavras = len(palavra)  # Retorna a quantidade de palavras dentro da frase.
print("Quantidade de palavras : {}".format(qtd_palavras))

sem_espacos = "".join(palavra) # Aqui eu tenho toda a frase junta sem os espaços.
print("Palavra sem os espaços : {}".format(sem_espacos))

qtd_letras = len(sem_espacos)
print("Quantidade de letras {}\n".format(qtd_letras))

palavra_invertida = ("")

for x in range ( qtd_letras -1, -1, -1 ):
	palavra_invertida = palavra_invertida + sem_espacos[x]
print("A palavra invertida é {}".format(palavra_invertida))
if palavra_invertida == sem_espacos:
	print("São palíndromos !!!")

else:
	print("Não são palíndromos ...")
