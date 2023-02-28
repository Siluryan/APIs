#### GITLAB

Coloque o nome desse arquivo de **config** no diretório das chaves ssh:
```sh
Host gitlab.com
User git
Port 22
Hostname gitlab.com
IdentityFile ~/.ssh/gitlab-main
TCPKeepAlive yes
IdentitiesOnly yes
```