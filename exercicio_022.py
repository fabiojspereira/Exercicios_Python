#nome_completo = str(input("Digite seu nome completo : ")).strip()
nome_completo = str(input("Digite seu nome completo : ")).strip()
print("Nome com todas as letras em maiúsculo : {}".format(nome_completo.upper()))
print("Nome com todas as letras em minúsculo : {}".format(nome_completo.lower()))

partes = nome_completo.split()
#qtd_partes = len(partes)
nome_limpo = nome_completo.strip() # Poderia jogar esse .strip() lá pro alto.
#qtd_caracteres_sem_espacos = (len(nome_limpo) - qtd_partes)+1

#print("Total de caracteres sem contar os espaços em branco : {}".format(qtd_caracteres_sem_espacos))
print("Total de caracteres sem contar os espaços em branco : {}".format(len(nome_limpo)-(nome_limpo.count(" "))))

primeiro_nome = len(partes[0])
print("A quantidade de letras do primeiro nome, que é {}, é {}.".format(partes[0].capitalize(), primeiro_nome))
