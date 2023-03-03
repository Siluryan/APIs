### Instalação do binário Go no LINUX

1 - Remova qualquer instalação prévia do Go, que geralmente vai estar em **/usr/local/go**
```bash
rm -rf /usr/local/go 
```
2 - Extraia o arquivo que você baixou do site no diretório **/usr/local** (**NUNCA** extraia o arquivo em cima de outro, tenha certeza de ter removido qualquer versão como indicado no passo 1)
```bash
tar -C /usr/local -xzf go1.20.1.linux-amd64.tar.gz
```
3 - Adicione o binário que você acabou de extrair como variável de ambiente do linux (desse modo o linux saberá onde procurar o binário)
```bash
export PATH=$PATH:/usr/local/go/bin
```
4 - Reinicie o computador. Após isso você pode checar se a instalação correu bem com o seguinte comando:
```bash
go version
```