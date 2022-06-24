import math

print('Lembre-se de usar PONTOS em vez de vírgulas para separar os centavos\n')
lista = list()
tabela = list()
tabela_master = list()
total_input = int(input('Quantos produtos quer adicionar? \n'))

for i in range(total_input):
	#nome do produto, valor de compra e valor de venda
	nome_produto = str(input(f'Digite o NOME do produto {int(i)+1}: '))
	valor_compra = float(input(f'Digite o valor de COMPRA do produto {int(i)+1}: '))
	valor_venda = float(input(f'Digite o valor de VENDA do produto {int(i) + 1}: '))

	#cria o par: valor de compra e valor de venda
	compra_venda = list()
	compra_venda.append(valor_compra)
	compra_venda.append(valor_venda)
	tabela.append(nome_produto)
	tabela.append(compra_venda)

	#coloca o par na tabela principal
	tabela_master.append(tabela)

	i += 1

#coloca os valores numa lista para ser possível a iteração
for i in tabela_master:
	for v in i[1]:
		lista.append(v)

#usa a lib math para poder comparar o tipo float
v = 0
a = 0
b = 1
for v in range((len(lista)-1)):
	if a > (len(lista)-1):
		pass
	else:
		compra = lista[a]
		venda = lista[b]
		diferenca = venda - compra
		if math.isclose(diferenca, compra/10) or (diferenca < compra/10):
			print(f'{tabela[v]}: menor ou igual a 10%')
		elif math.isclose(diferenca, compra/5) or (diferenca < compra/5):
			print(f'{tabela[v]}: menor ou igual a 20%')
		else:
			print(f'{tabela[v]}: maior que 20%')
		a += 2
		b += 2
		v += 2
