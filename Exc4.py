salario = float(input(print("Qual o Valor do salario: ")))
porcentagem = float(input(print("Quantos porcentos será o aumento: ")))
aumento = salario * porcentagem / 100
totalsal = salario + aumento

print ("O valor do aumento é: ",aumento)
print ("O valor total do salario é: ", totalsal)