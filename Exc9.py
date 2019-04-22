cigarros = int(input(print("Informe quantos cigarros você fuma por dia:")))
anos = int(input(print("Por quantos anos você fuma ou fumou:")))
minperdidodia = cigarros * 10
totaldias = int(((((minperdidodia * 365)/60)/24) * anos))

print("Voce perdeu ja perdeu",totaldias,"de dias de vida!!")
