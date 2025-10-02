print("hello World")


nomeEmpresa = input('digite nome da empresa: ')  # nome do fornecedor do item
# nome do item depois pretendo criar categoria como manutenção ou desgaste
nomeProduto = input('digite nome do produto: ')
# valor do produto livre de impostos
valorProduto = int(input('digite valor do produto: '))
# valor já calculado pela transportadora dps faço uma base de calculo baseado no peso x valor NF
frete = int(input('digite valor do frete: '))
# tenho que fazer o calculo de de ipi e icms e aliquota , mas por hora vai ser um valor já definido pelo user
imposto = int(input("imposto:"))
prazo = int(input("prazo:"))  # prazo para chegar a peça ao cliente

cet = sum([valorProduto, frete, imposto])

print(cet)
