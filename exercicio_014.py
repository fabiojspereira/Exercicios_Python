temp_c = float(input("Digite a temperatura em Celsius (ºC) a ser convertida para Fahrenheit (ºF) e Kelvin (K) : "))

temp_f = ((temp_c * 9)/5)+32
temp_k = (temp_c + 273.15)

print ("A temperatura de {:.2f} ºC corresponde à {:.2f} ºF e {:.2f} (K).".format(temp_c,temp_f,temp_k))
