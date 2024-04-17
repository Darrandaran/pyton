lista = []
valor = []
final = []
                        
for lista in range(1,5):
    produto = (input ("digite seu produto: "))
    preco = int(input ("Digite o valor do produto: "))
    valor.append(preco)
    lista.append(produto)
    print(lista, valor)
    

print(lista)

for aqui in range(1,5):
    desconto = valor*(0.5*100)/100
    print("O valor do desconto é:".format(desconto))

    final = valor - desconto
    print("O valor final será" .format(final))