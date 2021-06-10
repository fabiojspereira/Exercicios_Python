from math import sin, cos, tan, radians

angulo = float(input("Digite o valor do ângulo : "))

print("O SENO do ângulo de {}º é : {:.2f}º\nO COSSENO é : {:.2f}º\nE a tangente é :{:.2f}"
      .format(angulo, sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))

# É necessário primeiro transformar a variável ANGULO em RADIUS pra depois calcular SEN COS e TAN
# math.cos(x)
# Return the cosine of x radians.

# import math
# print ("O SENO do ângulo de {}º é : {:.2f}º\nO COSSENO é : {:.2f}º\nE a tangente é :{:.2f}"
#       .format( angulo, math.sin(math.radians(angulo)), math.cos(math.radians(angulo)),math.tan(math.radians(angulo))))
