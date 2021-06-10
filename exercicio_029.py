from time import sleep

vel_car = float(input("Favor digitar a velocidade do carro no determinado trecho : "))

km_acima = vel_car - 80
multa = km_acima * 7

if vel_car > 80:
    print("\nATENÇÃO !!! Sua velocidade registrada foi de {:.0f} km/h. Acima do limite permitido de 80 km/h.".format(vel_car))
    sleep(3)
    print("\nA multa por ultrapassar o limite de velocidade é de R$ 7,00 por km/h excedido.")
    print("Calculando o valor da sua multa ...")
    sleep(3)
    print("\nSerá cobrado o valor R$ {:.2f} por execesso de velocidade no trecho.".format(multa))
else:
    print("\nVelocidade registrada de {} km/h. Dentro do limite permitido de 80 km/h.".format(vel_car))
