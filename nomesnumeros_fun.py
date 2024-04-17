nomes = []
numeros = []
for i  in range(5):
    nome = str(input("Digite o {} nome:".format(i+1)))
    nomes.append(nome)

for i  in range(5):
    numero = input("Digite {} um número:" . format(i+1))
    numeros.append(numero)

print("\nOs nomes digitados foram:")
for i in nomes:
    print(i)

print("\nOs nomes digitados foram:")
for i in numeros:
    print(i)
