def abrir(caminho):
	caminho = open(caminho)
	print(caminho.read(),'\n')


caminho = '/home/guilherme/Which field in the IPv6 header points to optional'

	
for i in range(3):
	abrir(caminho)


print(caminho)


diretorio = input('Diretório do arquivo: ')
caminho = open(diretorio,'r+')


def escrever(caminho):
	caminho.write(input('Digite a frase que irá sobrescrever o arquivo: '))


escrever(caminho)


print(caminho.read())
