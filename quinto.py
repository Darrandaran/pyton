soma = 0
quantidade = 0
media = 0

#loop para solicitar números e calcular a média quanto for menor que 100 
while media < 100:
    numero = float(input("Digite um número:"))
    soma += numero
    quantidade += 1

#Calculando a média
    media = soma/quantidade 
    print("a média atual é:", media)