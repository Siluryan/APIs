- How to ssh into Kind cluster nodes with containerd runtime:

		docker exec -it node-name sh

	link: https://stackoverflow.com/questions/69108075/how-to-ssh-into-kind-cluster-nodes-with-containerd-runtime
	
- Open NGINX from our browser using Kind:

		kubectl port-forward svc/service-name 8081:80
	
	link: https://octopus.com/blog/testing-with-kind	

	
- Kubernetes Examples (pods, deployments, etc) using kubectl plugin:

	- Download precompiled binaries:
	
		https://github.com/seredot/kubectl-example/releases
	
	- Extract the binary and move into the directory created, them apply this command:
	
			sudo mv ./kubectl-example /usr/local/bin
	
	- Now you can use kubectl example:
	
			kubectl example pod
	
	link: https://github.com/Siluryan/kubectl-example
	
	
- Kubernetes Ingress:

	link: https://blog.getupcloud.com/kubernetes-ingress-c781dba08068
	
	
- Deploying WordPress and MySQL with Persistent Volumes:

	link: https://kubernetes.io/docs/tutorials/stateful-application/mysql-wordpress-persistent-volume/
