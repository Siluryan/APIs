while True:

	
	try:
		diretorio = input('Diretório do arquivo: ')
		caminho = open(diretorio)
		print(f'\nConteúdo do arquivo: {caminho.read()}')
		caminho.close()
		
	except FileNotFoundError as error:
		print('\nO arquivo não foi encontrado!')
		break


	try:
		diretorio = input('\nConfirme o diretório do arquivo: ')
		caminho = open(diretorio,'r+')
		
	except FileNotFoundError as error:
		print('\nO arquivo não foi encontrado!')
		break


	def escrever(caminho):
		caminho.write(input('\nDigite a frase que irá sobrescrever o arquivo: '))
		caminho.close()


	escrever(caminho)
	

	caminho = open(diretorio)
	print(f'\nConteúdo do arquivo: {caminho.read()}')
	caminho.close()
	break
