valor = float(input('Valor a ser calculado: \n'))

def kwargs_teste(valor, **kwargs):
    valor_desconto = kwargs.get('chave_desconto')
    print(f'valor do desconto: {valor_desconto}')

    if valor_desconto:
        total = valor - valor_desconto

    return total

kwargs_start = kwargs_teste(valor, chave_desconto = float(input('Valor do desconto: ')))
print(kwargs_start)
