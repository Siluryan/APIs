# Dia 1

## Questão 1

- Criar um pod utilizando a imagem do Nginx 1.18.0 com o nome de giropops no namespace strigus.

## Resposta 1

Nessa caso, temos duas formas.
A primeira, utilizando somente a linha de comando:

```bash
kubectl run giropops --image nginx:1.18.0 --port 80 --namespace strigus
```

```bash
A segunda, e a mais recomendada pelo fato de você poder analisar com mais cuidado o que está sendo implementado.

kubectl run giropops --image nginx:1.18.0 --port 80 --namespace strigus --dry-run=client -o yaml > pod.yaml

kubectl create -f pod.yaml
```

## Questão 2

- Aumentar a quantidade de réplicas do deployment giropops, que estã utilizando a imagem do nginx 1.18.0, para 3 replicas. O deployment esta no namespace strigus.

## Resposta 2

 ```bash
kubectl scale deployment giropops -n strigus --replicas 3
```

 ```bash
kubectl create deployment giropops -n strigus --image nginx:1.18.0 --port 80 --replicas 3 --dry-run=client -o yaml > deployment.yaml

kubectl apply -f deployment.yaml
```

 ```bash
kubectl edit deployment giropops -n strigus 
```

## Questão 3 

- Precisamos atualizar a versao do Nginx do Pod giropops. Ele está na versão 1.18.0 e precisamos atualizar para a versão 1.21.1 

## Resposta 3

```bash
kubectl edit pod giropops -n strigus
```

```bash
kubectl set image pod giropops -n strigus web=nginx1.21.0
```

```bash
kubectl get pods giropops -n strigus -o yaml > pod.yaml
# remover parametros desncessários
kubectl apply -f pod.yaml
```
