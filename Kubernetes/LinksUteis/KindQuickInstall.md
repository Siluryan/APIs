## Guia rápido de configuração do Kind

Copie o arquivo [kind_install.sh](https://github.com/Siluryan/Diversos/blob/main/Kubernetes/LinksUteis/kind_install.sh) para o seu computador, abra um terminal no local onde salvou o arquivo, e digite o seguinte comando:

```bash
sudo chmod 777 kind_install.sh && ./kind_install.sh
```

Link para o arquivo: [kind_install.sh](https://github.com/Siluryan/Diversos/blob/main/Kubernetes/LinksUteis/kind_install.sh)

Após executar esse script basta criar seu cluster com o comando **kind create cluster --name [nome_do_seu_cluster_sem_colchetes]** e testar os comandos do kubectl.
