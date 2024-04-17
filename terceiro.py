soma=0
contador=0

print("Digite o número para calcular a media.Digite 0(zero)para terminar.")

while True:
    valor = float(input("Digite um número:"))
    if valor == 0:
        break
    soma += valor
    contador +=1
if contador == 0:
    print("nehum numero foi inserido.")
else:
    media:soma/contador
    print("a media dos numeros inseridos é", media)