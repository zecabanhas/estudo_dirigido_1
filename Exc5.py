mercadoria = float(input(print("Qual o Valor da mercadoria: ")))
porcentagem = float(input(print("Quantos porcentos será o desconto: ")))
desconto = mercadoria * porcentagem / 100
totaldesc = mercadoria - desconto

print ("O valor do desconto é: ",desconto)
print ("O valor total a pagar pela mercadoria é: ", totaldesc)