#!/bin/sh
sudo apt-get install -y wget
wget https://go.dev/dl/go1.19.3.linux-amd64.tar.gz
sudo rm -rf /usr/local/go && sudo tar -C /usr/local/ -xzf go1.19.3.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin

sudo go install sigs.k8s.io/kind@v0.17.0
sudo echo -e "br_netfilter\nip_vs\nip_vs_rr\nip_vs_sh\nip_vs_wrr\nnf_conntrack_ipv4\noverlay" >> /etc/modules-load.d/k8s.conf

sudo echo -e "net.bridge.bridge-nf-call-ip6tables = 1\n
net.bridge.bridge-nf-call-iptables = 1\n
net.ipv4.ip_forward = 1" >> /etc/sysctl.d/k8s.conf

sudo sysctl --system

sudo apt-get update    
sudo apt-get install -y ca-certificates curl gnupg lsb-release
	
sudo rm -rf /etc/apt/keyrings && sudo mkdir -f -p /etc/apt/keyrings

sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
	
sudo echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo rm -rf /etc/containerd && sudo mkdir -p /etc/containerd
sudo containerd config default > /etc/containerd/config.toml

sudo systemctl enable containerd
sudo systemctl restart containerd

sudo apt-get update && sudo apt-get install -y apt-transport-https gnupg2
sudo curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" > /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl	

sudo swapoff -a
sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab

sudo kubeadm config images pull --cri-socket /run/containerd/containerd.sock

sudo rm -rf $HOME/.kube && mkdir -p $HOME/.kube
sudo rm -rf $HOME/.kube/config && cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
chown $(id -u):$(id -g) $HOME/.kube/config
