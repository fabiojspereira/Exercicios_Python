from datetime import datetime

cadastro = dict()

cadastro["nome"] = str(input("Digite o nome do funcionário : "))

ano_nascimento = int(input("Digite o ano de nascimento : "))
ano_atual = datetime.now()
idade = ( ano_atual.year - ano_nascimento )
cadastro["idade"] = idade

cadastro ["ctps"] = str(input("Digite o número da CTPS [ Digite '0' caso não tenha ] : "))

if cadastro ["ctps"] != "0" :
	cadastro ["ano contrato"] = int(input("Digite o ano de contratação do funcionário : "))
	cadastro ["salário"] = float(input("Digite o salário do funcionário : "))
	ano_aposentadoria = ( cadastro ["ano contrato"] - ano_nascimento ) + 35
	cadastro["aposentadoria"] = ano_aposentadoria

print()
print(cadastro)
print()
for chave, valor in cadastro.items() :
	print(f"- {chave:<14}{'tem o valor :':<10} {valor:<8}")
