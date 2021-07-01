dict_aluno = dict()

nome = str(input("Digite o nome do aluno : "))
dict_aluno ["nome"] = nome

dict_aluno ["media"] = float(input(f"Digite a média do aluno {dict_aluno['nome']} : "))

if dict_aluno ["media"] >= 7 :
	dict_aluno ["status"] = "APROVADO"
elif 5 <= dict_aluno ["media"] < 7 :
	dict_aluno ["status"] = "RECUPERAÇÃO"
else :
	dict_aluno ["status"] = "REPROVADO"

print()
for chave, valor in dict_aluno.items() : # O .tens() contém os dois valores : Chave e Valor.
	print(f"- {chave:<7}{'é igual a ':<10}{valor}")

'''
print(dict_aluno.keys())
print(dict_aluno.values())
print(dict_aluno.items())
'''
