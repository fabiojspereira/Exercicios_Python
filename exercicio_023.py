numero = int(input("Digite um número qualquer entre 0 e 9999 : "))

u = int(numero / 1 % 10)
d = int(numero / 10 % 10)
c = int(numero / 100 % 10)
m = int(numero / 1000 % 10)

print("Casa das unidades : {}".format(u))
print("Casa das dezenas : {}".format(d))
print("Casa das centenas : {}".format(c))
print("Casa dos milhares : {}".format(m))
