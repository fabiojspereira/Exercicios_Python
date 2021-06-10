frase = str(input("Digite uma frase qualquer : ")).strip()
qtd_a = frase.lower().count('a')
print("A quantidade de caracteres 'a' na frase é : {}.".format(qtd_a))

pos_p_a = frase.lower().find('a')+1 # posição do primeiro caracter 'a'. '+1' só pra ficar apresentável.
print("A posição do primeiro caractere 'a' na frase é : {}".format(pos_p_a))

pos_a_f = frase.lower().rfind('a')+1
print("A posição do último caractere 'a' é : {}.".format(pos_a_f))
