matrix_load = [ [], [], [], [], [], [], [], [], [] ]
#				 1   2   3   4   5   6   7   8   9
count = 0

for linha in range ( 0, 3 ) :
	for coluna in range ( 0 , 3 ) :
		n = int(input(f"Digite o valor para [{linha},{coluna}] : "))
		matrix_load[count].append(n)
		count += 1

print(matrix_load[0:3])
print(matrix_load[3:6])
print(matrix_load[6:9])
