dias_alugado = int(input("Por quantos dias o carro foi alugado ? "))
km_percorrido = float(input("Quantos quilômetros o veículo percorreu ? "))

valor_diaria = (dias_alugado * 60)
valor_km = (km_percorrido * 0.15)

print("Será cobrado o valor de R$ {:.2f} por {} dias alugado.\nE um adicional de R$ {:.2f} por {:.0f} quilômetros rodados.".format(
    valor_diaria, dias_alugado, valor_km, km_percorrido))
