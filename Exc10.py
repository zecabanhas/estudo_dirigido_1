import math

metros = float(input(print("Digite quantos metros quadrados de area a ser pintada")))

opcao = int(input(print("Digite 1 para comprar latas de 18 litros \n"
                        "Digite 2 para comprar latas de 3,6litros \n"
                        "Digite 3 para comprar latas mescladas:")))

metros_litro = 6.0


if opcao == 1:
    latas_grandes = metros/(18 * metros_litro)
    latas_grandes = math.ceil(latas_grandes)
    valor = latas_grandes * 80
    print("Voce usara",latas_grandes,"para pintar",metros,"metros quadrados, no valor de",valor,"reais")

elif opcao == 2:
    latas_pequenas = metros / (3.6 * metros_litro)
    latas_pequenas = math.ceil(latas_pequenas)
    valor2 = latas_pequenas * 25

else :
    print("Opção Incorreta!")







