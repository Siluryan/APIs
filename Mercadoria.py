import math

print('Lembre-se de usar PONTOS em vez de vírgulas para separar os centavos\n')
lista = list()
tabela = list()
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
	i += 1

#coloca os valores numa lista para ser possível a iteração
idx = 1
if total_input == 1:
	lista.append(valor_compra)
	lista.append(valor_venda)

for i in tabela:
	if idx > len(tabela):
		pass
	else:
		lista.append(tabela[idx])
		idx += 2

#usa a lib math pra poder comparar o tipo float
v = 0
if total_input == 1:
	compra = valor_compra
	venda = valor_venda
	diferenca = venda - compra
	if math.isclose(diferenca, compra / 10) or (diferenca < compra / 10):
		print(f'{tabela[v]}: menor ou igual a 10%')
	elif math.isclose(diferenca, compra / 5) or (diferenca < compra / 5):
		print(f'{tabela[v]}: menor ou igual a 20%')
	else:
		print(f'{tabela[v]}: maior que 20%')

else:
	for i in lista:
		if v >= len(tabela):
			pass
		else:
			compra = i[0]
			venda = i[1]
			diferenca = venda - compra
			if math.isclose(diferenca, compra/10) or (diferenca < compra/10):
				print(f'{tabela[v]}: menor ou igual a 10%')
			elif math.isclose(diferenca, compra/5) or (diferenca < compra/5):
				print(f'{tabela[v]}: menor ou igual a 20%')
			else:
				print(f'{tabela[v]}: maior que 20%')
			v += 2
