nome = str(input("Digite seu nome completo : ")).strip()

nome_separado = nome.split()
print(nome_separado)
print(len(nome_separado))
print("-----------------------------------------")

primeiro_nome  = nome_separado[0]
#ultimo_nome_v1 = len(nome_separado)
#ultimo_nome_v2 = nome_separado[len(nome_separado)-1]
#ultimo_nome_v3 = nome_separado[4]

print("Print do lenght da variável 'len(nome_separado)' que retorna um número inteiro : {} ".format(len(nome_separado)))
print("Print do último item do conteúdo da lista 'nome_separado[len(nome_separado)-1]' : {}".format(nome_separado[len(nome_separado)-1]))
print("Print do item 2 da lista 'nome_separado[2]' : {}".format(nome_separado[2]))


#print(ultimo_nome_v1)
#print(ultimo_nome_v2)
#print(ultimo_nome_v3)



#print("Seu primeiro nome é : {}.".format(primeiro_nome))
#print("Seu último nome é : {}.".format(nome_separado))[len(nome_separado)-1]))
