print("Vamos calcular o valor do produto com desconto de 5% para pagamento a vista.")
produto = str(input("Qual o nome do produto ? "))
valor = float(input("Digite o valor do prouto : "))
desconto = (((valor * 5) / 100))
valor_desconto = (valor - desconto)

# print(valor)
# print (desconto)
# print(valor_desconto)

print("O produto {} tem preço padrão de R$ {:.2f}.\nCom desconto de 5% a vista ele passa a custar : R$ {:.2f}.".format(produto,valor,(valor-(((valor * 5) / 100)))))
print("Valor do desconto aplicado de 5% : R$ {:.2f}".format(desconto))
