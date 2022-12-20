Obs: Salvo indicação contrária, as configurações a seguir devem ser realizadas em todos os nodes (nesse exemplo estão sendo criados 3 nodes)

## 0. Portas
Portas a serem abertas nos nodes:

### MASTER
```yaml
- kube-apiserver = 6443 TCP
- etcd server API = 2379-2380 TCP
- kubelet API = 10250 TCP
- kube-scheduler = 10251 TCP
- kube-controller-manager = 10252 TCP
- kubelet API read-only = 10255 TCP
```
### WORKERS
```yaml
- kubelet API = 10250 TCP
- kubelet API read-only = 10255 TCP
- nodeport services = 30000-32767 TCP
```
## 1. /etc/hosts

Coloque o ip das instâncias EC2 que farão parte do cluster nesse arquivo.

Ex:    

    172.31.52.234 k8s-1
    172.31.63.119 k8s-2
    172.31.49.208 k8s-3
   
## 2. /etc/modules-load.d/k8s.conf
Alguns módulos do kernel precisam ser habilitados.

Coloque as informações a seguir nesse arquivo, do jeito que aparecem aqui:

    br_netfilter
    ip_vs_rr
    ip_vs_wrr
    ip_vs_sh
    nf_conntrack_ipv4
    ip_vs

## 3. /etc/sysctl.d/k8s.conf
Esse arquivo ainda não existe, você precisa criá-lo com as seguintes informações:


    net.bridge.bridge-nf-call-ip6tables = 1
    net.bridge.bridge-nf-call-iptables = 1
    net.ipv4.ip_forward = 1


## 4. yum install -y vim bash-completion wget
Apenas instale esse três pacotes.

Não se esqueça de fazer o update nos repositórios antes da instalação, assim como 
reiniciar a máquina uma vez que foram habilitados módulos adicionais do kernel nas etapas anteriores.

## 5. /etc/yum.repos.d/k8s.repo
Crie esse arquivo também (os links devem ser digitados numa única linha):
```yaml
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo-gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
```

## 6. yum install -y kubelet kubeadm kubectl
Não se esqueça de habilitar permanentemente o kubelet (garantindo que ele funcione caso a instância precise ser reiniciada) com os seguintes comando:
```bash
systemctl enable kubelet
systemctl start kubelet
```

## 7.1 Baixe o containerD
Não se esqueça de procurar a versão mais recente, e use a url a seguir apenas como exemplo ou referência:

Comando (tudo na mesma linha):

    wget https://github.com/containerd/containerd/releases/download/v1.2.1/containerd-1.2.1.linux-amd64.tar.gz

## 7.2 Descompacte o arquivo que você baixou e já coloque esses binários no /usr/local/
Comando:

    tar -xvzf containerd-1.2.1.linux-amd64.tar.gz -C /usr/local/

## 8.1 Baixe o runC e já o redirecione pro local apropriado
Não se esqueça de procurar a versão mais recente, e use a url a seguir apenas como exemplo ou referência:

Comando (tudo na mesma linha - tem um espaço entre runc e https):

    wget -O /usr/local/sbin/runc https://github.com/opencontainers/runc/releases/download/v1.0.0-rc6/runc.amd64

## 8.2 Dê ao runC a permissão de execução
Comando:

    chmod 755 /usr/local/sbin/runc

## 9. Baixe as configurações do containerD que devem ser passadas ao SystemD e já as adicione ao diretório apropriado
Comando:

    curl -o /etc/systemd/system/containerd.service https://raw.githubusercontent.com/containerd/cri/master/contrib/systemd-units/containerd.serivce

## 10. Reinicie o daemon do systemctl e habilite o serviço do containerD
Comando:
```bash
    systemctl daemon-reload
    systemctl enable containerd.service
    systemctl start containerd.service
```

## 11.1 Informe ao CRI que ele deverá usar o containerD
O CRI é um plugin que habilita o kubelet a usar uma variedade de container runtimes.

Comando:

    echo "runtime-endpoint: unix:///run/containerd/containerd.sock" > /etc/crictl.yaml

## 11.2 /etc/systemd/system/kubelet.service.d/0-containerd.conf
Esse arquivo também deve ser criado com as seguintes informações:
```yaml
[Service]
Environment="KUBELET_EXTRA_ARGS=--container-runtime=remote --runtime-request-timeout=15m --container-runtime-endpoint=unix:///run/containerd/containerd.sock"
```
## 12. Reinicie o daemon do systemctl
Comando:

    systemctl daemon-reload

## 13. Para efeito de testes ou implementação em ambientes não críticos, desabilite o SElinux e o FirewallD
Em ambientes produtivos você precisará buscar as informações necessárias para configurar corretamente essas opções, assim como se certificar de estar em compliance com as normas ou regulamentos de sua empresa)

Comando:

    setenforce 0
    systemctl stop firewalld

## 14. Desabilite o swap
Não se esqueça de desabilitar permanentemente o swap no /etc/fstab (existem diversos tutoriais na internet pra isso).

Comando:

    swapoff -a

## 15. (Apenas na instância que será o node MASTER)
A partir desse momento você já consegue iniciar o seu cluster Kubernetes, mas você ainda precisará informar sobre as configurações do CRI nesse momento.

Comando:

    kubeadm init --cri-socket /run/containerd/containerd.sock

## 16. O restante da configuração é idêntica à um cluster que pode ser gerenciado pelo Docker:
Essas informações podem ser facilmente encontradas na internet, apenas coloquei o que deve ser feito.

    - Crie o diretório do kube/config
    - Instale o WeaveNet para a comunicação entre os pods
    
## 17. Use o kubeadm join para que os nodes workers entrem no cluster
**Importante:** você ainda precisará informar sobre as configurações do CRI nesse momento (apenas adicione o mesmo parâmetro no final do kubeadm join, do mesmo modo que você passou ao inicar o cluster com kubeadm init)

Ex (encurtado):
```md
kubeadm join 172.31.52.234:6443 --token k87a6d7s6d.e8adge6dge --cri-socket /run/containerd/containerd.sock
```