n = 0
while n >= 0:
	print("\nDeseja ver a tabuada de qual valor ? * Digite um valor negativo para sair do programa ")
	n = int(input(": "))
	if n < 0:
		break

	else:
		for count_01 in range (0,11,1):
			print(f"{n:^3}x{count_01:^5}={n * count_01:>5}")

print("Fim...")
