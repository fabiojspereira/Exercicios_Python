times = ("Corinthians","Palmeiras","Santos","Grêmio","Cruzeiro",
		 "Flamengo","Vasco","Chapecoense","Atlético-MG","Botafogo",
		 "Athletico","Bahia","São Paulo","Fluminense","Sport","Vitória",
		 "Coritiba","Avaí","Ponte Preta","Atlético-GO")

print("Classificação final do Campeonato Brasileiro : ")
for count in range ( 0, len(times) ) :
	print(f"{count + 1}º {times[count]}")

print("\nExibição dos 5 primeiros classificados : ")
#print(times[0:5])
for count in range ( 0, 5 ) :
	print(f"{count + 1}º {times[count]}")

#print(times[-4:])
print("\nExibição dos 4 últimos classificados : ")
for count in range ( -4, 0 ) :
	print(f"{count + 21}º {times[count]}")

print("\nExibição em ordem alfabética : ")
ordem = (sorted(times))
for count in range ( 0, len(ordem)):
	print(ordem[count])

#print(sorted(times))

print("\nPosição do clube Chapecoense :")
x = times.index("Chapecoense")+1
print("Posição : {}".format(x))
