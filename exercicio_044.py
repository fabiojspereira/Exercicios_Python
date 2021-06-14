import time

x = len("PROGRAMA PARA CÁLCULO DE FORMA DE PAGAMENTO DO PRODUTO")
print("*"* x )
print("PROGRAMA PARA CÁLCULO DE FORMA DE PAGAMENTO DO PRODUTO")
print("*"* x )

produto = str(input("Digite o nome do produto : "))
valor = float(input("\nDigite o valor do produto : "))

print('''
Selecione a forma de pagamento desejada :
\n1 - \033[1;34mPagamento à vista\033[m   - Dinheiro / Cheque		: 10% de desconto.
2 - \033[1;34mPagamento à vista\033[m   - Cartão Débito			: 5% de desconto.
3 - \033[1;34mPagamento Parcelado\033[m - 2x no Cartão			: Valor Normal sem desconto.
4 - \033[1;34mPagamento Parcelado\033[m - 3x ou mais no Cartão	: \033[1;33mValor com acréscimo de 20% de juros.\033[m''')
opt = int(input("\nDigite a opção desejada : "))

if opt == 1:
	print("Calculando valor ...")
	time.sleep(0.5)
	print("\nForma de pagamento selecionada : ")
	valor_novo = valor - ( valor * 10 ) / 100
	print("1 - \033[1;32mPagamento à vista\033[m - Dinheiro / Cheque : 10% de desconto.\n\nProduto            : {}\nValor a ser pago   : R$ {:.2f}\nDesconto concedido : R$ {:.2f}.".format(produto,valor_novo,valor - valor_novo))

elif opt == 2:
	print("Calculando valor ...")
	time.sleep(0.5)
	print("\nForma de pagamento selecionada : ")
	valor_novo = valor - ( valor * 5 ) / 100
	print("2 - \033[1;32mPagamento à vista\033[m - Cartão Débito : 5% de desconto.\n\nProduto            : {}\nValor a ser pago   : R$ {:.2f}.\nDesconto concedido : R$ {:.2f}.".format(produto,valor_novo,valor - valor_novo))

elif opt == 3:
	print("Calculando valor ...")
	time.sleep(0.5)
	print("\nForma de pagamento selecionada : ")
	valor_novo = valor / 2
	print("3 - \033[1;32mPagamento Parcelado\033[m - 2x no Cartão : Valor Normal sem desconto.\n\nProduto            : {}\nValor a ser pago   : 2 parcelas x R$ {:.2f}.\nDesconto concedido : R$ {:.2f}.".format(produto,valor_novo,valor - 2 * valor_novo))

elif opt == 4:
	qtd_par = int(input("\nEm quantas parcelas ( 3x,4x,5x,6x,7x,8x,9x ou 10x ) será feita a compra ? "))
	if qtd_par >= 3 and qtd_par <= 10:
		print("Calculando valor ...")
		time.sleep(0.5)
		print("\nForma de pagamento selecionada : ")
		valor_novo = valor + ( valor * 20 ) / 100
		print("4 - \033[1;32mPagamento Parcelado\033[m - 3x ou mais no Cartão	\n\nProduto                : {}\nQuantidade de parcelas : {} x de {:.2f}\nValor a ser pago       : R$ {:.2f}. \033[1;33mcom acréscimo de R$ {:.2f} ( 20% ).\033[m".format(produto, qtd_par, ( valor_novo / qtd_par ),valor_novo,( valor * 20 ) / 100))
