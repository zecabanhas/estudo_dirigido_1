import math

metros = float(input("Digite quantos metros quadrados de area a ser pintada: "))

opcao = int(input("Digite 1 para comprar latas de 18 litros :\n"
                        "Digite 2 para comprar latas de 3,6litros: \n"
                        "Digite 3 para comprar latas mescladas: \n"))

metros_litro = 6.0


if opcao == 1:
    latas_grandes = metros/(18 * metros_litro)
    latas_grandes = math.ceil(latas_grandes)
    valor = latas_grandes * 80
    print("1)Voce usara",latas_grandes,"para pintar",metros,"m², no valor de",valor,"reais")

elif opcao == 2:
    latas_pequenas = metros / (3.6 * metros_litro)
    latas_pequenas = math.ceil(latas_pequenas)
    valor2 = latas_pequenas * 25
    print("2)Voce usara", latas_pequenas, "para pintar", metros, "m², no valor de", valor2, "reais")

elif opcao == 3:
    litros_metro = metros/metros_litro
    qtdGalao  = math.ceil((litros_metro / 3.6) * 1.10)
    qtdLata = math.ceil((litros_metro / 18)*1.10)
    compraLata = 80 * qtdLata
    compraGalao = 25 * qtdGalao
    melhor_lata = int(litros_metro / 18)
    melhor_galao = math.ceil((litros_metro % 18) / 3.6)
    compra_mix = (melhor_lata * 80) + (melhor_galao * 25)
    print("3) Compra de latas e galões de forma a pagar o menor valor:\nQuant. de latas: ", melhor_lata,
          "\nQuant. de galões: ", melhor_galao, "\nPreço Total: ", compra_mix, "\n")
else :
    print("Opção Incorreta!")





