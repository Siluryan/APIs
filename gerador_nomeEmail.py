''' Você precisa de um arquivo com uma lista de nomes, sem vírgulas, onde cada nome
deve estar em uma linha. Além disso, crie dois arquivos, um para a lista de nomes formatada e
um para a lista de emails que será gerada '''

import re
import mmap

lista_nomes = list()
lista_emails = list()
lista_intercalada = list()

def contar_linhas():
    with open("caminho pra sua lista crua", "r+") as myfile:
        mm = mmap.mmap(myfile.fileno(), 0)
        total_lines = 0

        while mm.readline():
            total_lines += 1

    return total_lines

total_lines = contar_linhas()

def linha_to_string():

    with open("caminho pra sua lista crua") as lista:
       
        linha = lista.readline(total_lines).replace('\n', ' ')
        lista_nomes.append(linha)

    with open("caminho pra sua lista crua", 'r') as fr:
        # reading line by line
        lines = fr.readlines() 
        
        # opening in writing mode
        with open("caminho pra sua lista crua", 'w') as fw:
            ptr = 1
            for line in lines:
                if ptr != 1:
                    fw.write(line)
                ptr += 1

def criar_email(lista):
    for i in lista:
        i = i.replace(" ", "")
        i = re.sub(r"[^a-zA-Z0-9]","",i)
        i = i.lower()+"@gmail.com"
        lista_emails.append(i)
        
        with open("caminho pra sua lista de emails", "a") as lista_final:   
            lista_final.write("%s\n" %i)
            lista.pop(0)            
            criar_email(lista)
                
for i in range(total_lines):
    linha_to_string()

with open("caminho pra sua lista de nomes", 'w') as temp_file:
    for item in lista_nomes:
        temp_file.write("%s\n" % item)

criar_email(lista_nomes)
