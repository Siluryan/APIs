# Dia 3 

## Questão 1

Criar um pod estático utilizando a imagem do nginx

O Kind não permite scp de forma nativa e portanto você precisa criar o Pod Estático manualmente. Existem algumas formas de fazer isso de dentro do node(consulte esse link caso não sabia como entrar num node provisionado pelo Kind [link](https://github.com/Siluryan/Diversos/tree/main/Kubernetes/Links-%C3%9Ateis))

cat << EOF > static-pod.yaml [enter]
digite seu texto [enter]
digite EOF [enter]

outra opção:

copie o texto que deseja colocar no arquivo para criação do static-pod;
dentro do node:
digite echo "[depois de abrir aspas aperte CTRL+SHIFT+V e feche as aspas na sequencia]" > static-pod.yaml

caso precise deletar linhas use:
cat -n static-pod.yaml (isso vai trazer o conteúdo do arquivo com as linhas enumeradas)
sed -i "nºd" static-pod.yaml (coloque o número da linha seguido pela letra d entre aspas para deletar)
caso precise substituir linhas:
sed -i "nºd" static-pod.yaml && sed -i "nºi texto-que-ira-substituir-o-antigo" static-pod.yaml (coloque o número da linha seguido pela letra d entre aspas para deletar e coloque o número da linha seguindo pela letra i e depois pelo texto para inserir)


