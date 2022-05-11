def abrir(caminho):
	caminho = open(caminho)
	print(caminho.read(),'\n')


caminho = input('Diretório do arquivo: ')

	
for i in range(3):
	abrir(caminho)


print(caminho,'\n')


diretorio = input('Diretório do arquivo: ')
caminho = open(diretorio,'r+')


def escrever(caminho):
	caminho.write(input('Digite a frase que irá sobrescrever o arquivo: '))


escrever(caminho)


print(caminho.read())
