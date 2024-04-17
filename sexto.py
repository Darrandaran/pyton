soma = 0


while soma < 200:
    numero = float(input("Digite um número:"))
    soma += numero

    soma +=(soma*10)/100

print("o resultado é:",soma)