dias = int(input(print("Digite o numero de dias: ")))
horas = int(input(print("Digite o numero de horas: ")))
minutos = int(input(print("Digite o numero de minutos")))
segundos = int(input(print("Digite o numero de segundos")))

total = ((dias * 86400) + (horas * 3600) + (minutos * 60) + segundos)

print("O total em segundos é:", total)