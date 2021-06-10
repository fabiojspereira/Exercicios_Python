print("Vamos calcular quantos dólares(US$) você poderá comprar com o real(R$) !")
print("Cotação do dólar no dia 25/03/2021 = R$ 5,67.")

qtd_real = float(input("Digite o valor que possui em reais(R$) : " ))
qtd_dolar = (qtd_real/5.67)
print("Com R$ {:.2f}, é possível comprar US$ {:.2f}.".format(qtd_real,qtd_dolar))




