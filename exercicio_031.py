distancia_km = int(input("Qual é a distância da viagem em km ? "))

if distancia_km <= 200:
    print("Distância abaixo de 200 km tem desconto ! Sua passagem irá custar : R$ {:.2f}.".format(distancia_km * 0.5))
else:
    print("Será cobrado o valor de R$ 0.50 por km de distância. O preço da passagem será de : R$ {:.2f}.".format(distancia_km * 0.45))
