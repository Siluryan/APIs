#!/bin/bash
sudo apt-get install -y wget
wget https://go.dev/dl/go1.19.3.linux-amd64.tar.gz
rm -rf /usr/local/go && tar -C /usr/local -xzf go1.19.3.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin

go install sigs.k8s.io/kind@v0.17.0
echo -e "br_netfilter\nip_vs\nip_vs_rr\nip_vs_sh\nip_vs_wrr\nnf_conntrack_ipv4\noverlay" >> /etc/modules-load.d/k8s.conf

echo -e "net.bridge.bridge-nf-call-ip6tables = 1\n
net.bridge.bridge-nf-call-iptables = 1\n
net.ipv4.ip_forward = 1" >> /etc/sysctl.d/k8s.conf

sysctl --system

apt-get update    
apt-get install ca-certificates curl gnupg lsb-release -y
	
mkdir -p /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
	
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

apt-get update
apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
mkdir -p /etc/containerd
containerd config default > /etc/containerd/config.toml

systemctl enable containerd
systemctl restart containerd

apt-get update && sudo apt-get install -y apt-transport-https gnupg2
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" > /etc/apt/sources.list.d/kubernetes.list
apt-get update
apt-get install -y kubelet kubeadm kubectl	

swapoff -a
sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab

kubeadm config images pull --cri-socket /run/containerd/containerd.sock

mkdir -p $HOME/.kube
cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
chown $(id -u):$(id -g) $HOME/.kube/config
