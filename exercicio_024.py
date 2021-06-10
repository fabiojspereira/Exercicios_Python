nome_cidade = str(input("Digite o nome de sua cidade : ")).strip()
print("Cidade digitada : {}.".format(nome_cidade))
nome_cidade_separada = nome_cidade.split()
#primeiro_parte_nome = nome_cidade_separada[0]

x = 'santo' in nome_cidade_separada[0].lower().strip()

print("A cidade digitada começa com a palavra 'Santo' ? ", x)







