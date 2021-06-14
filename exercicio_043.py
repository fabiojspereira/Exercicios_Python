x = len("PROGRAMA PARA CÁLCULO DE IMC")
print("*"* x )
print("PROGRAMA PARA CÁLCULO DE IMC")
print("*"* x )

nome = str(input("\nDigite o nome do paciente : ")).strip()
peso = float(input("Digite o peso do paciente : "))
altura = float(input("Digite a altura da pessoa em metros : "))

imc = peso / (altura ** 2)

if imc < 18.5:
	print("\n{}, você está \033[1;33mabaixo do peso\033[m.\nÍndice de Massa Corporia ( IMC ) : {:.1f}.".format(nome,imc))
elif imc >= 18.5 and imc < 25:
	print("\n{}, você está no \033[1;34mpeso ideal\033[m.\nÍndice de Massa Corporia ( IMC ) : {:.1f}.".format(nome,imc))
elif imc >= 25 and imc < 30:
	print("\n{}, você está com \033[1;33msobrepeso\033[m.\nÍndice de Massa Corporia ( IMC ) : {:.1f}.".format(nome, imc))
elif imc >= 30 and imc < 40:
	print("\n{}, você está com \033[1;31mobesidade\033[m.\nÍndice de Massa Corporia ( IMC ) : {:.1f}.".format(nome, imc))
else:
	print("\n{}, você está com \033[1;31mobesidade mórbida\033[m. Índice de Massa Corporia ( IMC ) : {:.1f}.".format(nome, imc))
