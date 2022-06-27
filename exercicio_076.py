produtos = ("Lápis",1.75,"Borracha",2.00,"Caderno",15.90,"Estojo",25.00,"Transferidor",4.20,"Compasso",9.99,"Mochila",120.32,"Canetas",22.30,"Livro",34.90)

print("-"*65)
print("{:^65}".format("LISTAGEM DE PREÇOS"))
print("-"*65)

for count in range ( 0, len(produtos), 2 ):
	print("{:.<53}{}{:>8.2f}".format(produtos[count]," R$ ",produtos[count+1]))
print("-"*65)
