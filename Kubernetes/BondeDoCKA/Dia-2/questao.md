# Dia2 

## Questão 1

- Quantos nodes são workers?
	
	kubectl get nodes

- Qual o Pod Network (CNI) que estamos utilizando?

	kubectl get pods -n kube-system

- Qual o CIDR dos pods no segundo worker?
	
	kubectl describe nodes/nome-do-segundo-worker | grep -i pod 
	
	kubectl get nodes meuk8s-worker -o yaml | grep -i cidr
	
	kubectl get node -o jsonpath="{range.items[*]}{.metadata.name}{.spec.podCIDR}
	
	kubectl cluster-info dump | grep -i cidr > kube-dump.txt && head -n 4 kube-dump.txt // coloque como parâmetro do head o dobro do número que você possui de nodes
	
- Qual é o serviço de DNS para o cluster?

	kubectl get pods -n kube-system
	
## Questão 2

- Crie um pod com as seguintes características:

	- Precisa ter um container rodando a imagem do nginx
	
	- Precisa ter outros 2 containers com a imagem do busybox, o primeiro imprimindo um conteudo no arquivo /tmp/index.html e o segundo aplicando um tail -f no arquivo gerado no primeiro container

[pods.yaml]:https://github.com/Siluryan/Diversos/blob/main/Kubernetes/BondeDoCKA/Dia-2/pods.yaml
