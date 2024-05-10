#definindo tupla com produtos e seus valores

produtos = (
    ("produtos1", 10),
    ("produtos2", 20),
    ("produtos3", 30),
    ("produtos4", 40),
    ("produtos5", 50)
)

#calcule a soma dos valores do produto
soma = sum(valor for _, valor in produtos)

#verificando se a soma é maior q 200 e aplicando o desconto
if soma > 200:
    desconto = soma * 0.10 #desconto 10%
elif soma <= 200:
    desconto = soma * 0.05 #desconto 5%

#aplicando desconto se necessário
soma -= desconto

print("o valor total dos produtos é:", soma)
