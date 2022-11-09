## Guia rápido de configuração do Kind

Abaixo estão os passos necessários para que você possa usar o Kind na sua máquina. No entanto, se por qualquer razão quiser fazer isso automaticamente, copie o arquivo [kind_install.sh](https://github.com/Siluryan/Diversos/blob/main/Kubernetes/LinksUteis/kind_install.sh) pro seu computador, abra um terminal no local onde salvou o arquivo, e digite o seguinte comando:

```bash
sudo chmod 777 kind_install.sh && ./kind_install.sh
```

Link para o arquivo: [kind_install.sh](https://github.com/Siluryan/Diversos/blob/main/Kubernetes/LinksUteis/kind_install.sh)

Após executar esse script basta criar seu cluster com o comando **kind create cluster --name [nome_do_seu_cluster_sem_colchetes]** e testar os comandos do kubectl.

### 1. Instalação do Kind


1.1 Certifique-se de ter o Go instalado na sua máquina:

```bash
go version
```

1.2 Caso não tenha o Go instalado, acesse esse link para ver como realizar a instalação:

```
https://go.dev/doc/install
```

1.2 Se a versão do seu Go for inferior a 1.17:
    
!AVISO: USE DOIS SINAIS DE MAIOR (>>), SE USAR APENAS UM IRÁ SOBRESCREVER TODO O ARQUIVO!
        
```bash
sudo echo 'export GO111MODULE="on"' >> ~/.profile 
```	

1.3 Instalar o Kind:

```bash
go install sigs.k8s.io/kind@v0.17.0
```
	
### 2. Configuração do sistema: 

2.1 Módulos do kernel:

```bash
sudo echo -e "br_netfilter\nip_vs\nip_vs_rr\nip_vs_sh\nip_vs_wrr\nnf_conntrack_ipv4\noverlay" >> /etc/modules-load.d/k8s.conf
```

2.2 Permitindo tráfego no iptables:

```bash
sudo echo -e "net.bridge.bridge-nf-call-ip6tables = 1\n
net.bridge.bridge-nf-call-iptables = 1\n
net.ipv4.ip_forward = 1" >> /etc/sysctl.d/k8s.conf
```

2.3 Habilitando as novas configurações:

```bash
sudo sysctl --system
```

### 3. Instalação do containerd

Obs: Caso não esteja usando o Ubuntu ou outras distribuições baseadas em Debian, pesquise na internet como instalar o containerd na sua distribuição (estou presumindo que você tem bom senso e usa Linux :)


3.1 Habilitando o uso do repositório com HTTPS:

```bash
sudo apt-get update
    
sudo apt-get install ca-certificates curl gnupg lsb-release
```

3.2 Adicionando a key:	

```bash 	
sudo mkdir -p /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
``` 

3.3 Registrando o repositório:

```bash 	
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

3.4 Instalando componentes do Docker:

Obs: Você pode instalar apenas o containerd.io, mas em alguns casos você vai precisar do docker para interagir com seu cluster, e portanto o melhor a se fazer é configurar todos os componentes de uma vez

```bash
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

3.5 Criando o diretório de configurações do containerd:

```bash	
mkdir -p /etc/containerd

containerd config default > /etc/containerd/config.toml
```

3.6 Habilitando o containerd:

```bash	
sudo systemctl enable containerd

sudo systemctl restart containerd
```

### 4. Instalação do kubeadm

```bash
sudo apt-get update && sudo apt-get install -y apt-transport-https gnupg2

curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

sudo echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" > /etc/apt/sources.list.d/kubernetes.list

sudo apt-get update

sudo apt-get install -y kubelet kubeadm kubectl	
```

### 5. Desabilitar a swap

```bash
sudo swapoff -a

sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
```

### 6. Configurar o containerd como plugin do kubeadm

```bash
sudo kubeadm config images pull --cri-socket /run/containerd/containerd.sock
```

### 7. Configuração do diretório do kubeadm

```bash
mkdir -p $HOME/.kube

cp -i /etc/kubernetes/admin.conf $HOME/.kube/config

sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

Nesse ponto você já deve conseguir usar o Kind normalmente
	



	
	
	
	
