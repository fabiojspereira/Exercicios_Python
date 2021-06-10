from datetime import date

ano = int(input("Digite um ano e irei analisar se ele foi um ano bissexto ou ano comum.\nDigite '0' caso queira saber o ano atual : "))

if ano == 0:
    ano = date.today().year
    print ("Ano atual é : {}.".format(ano))

    # Para ser bissexto é necessário as seguintes regras :

    # REGRA 1 De 4 em 4 anos é ano bissexto.
    # REGRA 2 De 400 em 400 anos é ano bissexto.
    # REGRA 3 De 100 em 100 anos não é ano bissexto.

       # REGRA 1              REGRA 3               REGRA 2
if ( ano % 4 == 0 ) and ( ano % 100 != 0 ) or ( ano % 400 == 0 ) :
    print ("Ano Bissexto.")
else:
    print("Ano normal.")
