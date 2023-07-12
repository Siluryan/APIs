import csv
import subprocess
import yaml

def get_pod_info(node_name):
    cmd = f"kubectl get pods --all-namespaces -o yaml --field-selector spec.nodeName={node_name}"
    output = subprocess.check_output(cmd, shell=True).decode()
    data = yaml.safe_load(output)
    pod_info = []

    for item in data['items']:
        namespace = item['metadata']['namespace']
        pod_name = item['metadata']['name']
        container_specs = item['spec']['containers']

        for container in container_specs:
            metrics = {
                'Namespace': namespace,
                'Pod Name': pod_name,
                'CPU Requests': container['resources'].get('requests', {}).get('cpu', ''),
                'Memory Requests': container['resources'].get('requests', {}).get('memory', ''),
                'CPU Limits': container['resources'].get('limits', {}).get('cpu', ''),
                'Memory Limits': container['resources'].get('limits', {}).get('memory', ''),
                'CPU Usage': '',
                'Memory Usage': ''
            }

            cpu_request = metrics['CPU Requests']
            if cpu_request.isdigit():
                cpu_request = f"{int(cpu_request) * 1000}m"
                metrics['CPU Requests'] = cpu_request

            cpu_limit = metrics['CPU Limits']
            if cpu_limit.isdigit():
                cpu_limit = f"{int(cpu_limit) * 1000}m"
                metrics['CPU Limits'] = cpu_limit
       
            try:
                usage_cmd = f"kubectl top pod {pod_name} -n {namespace} --no-headers"
                usage_output = subprocess.check_output(usage_cmd, shell=True).decode().strip()
                if usage_output:
                    cpu_usage, memory_usage = usage_output.split()[-2:]  
                    metrics['CPU Usage'] = cpu_usage
                    metrics['Memory Usage'] = memory_usage
            except subprocess.CalledProcessError:
                metrics['CPU Usage'] = 'Error'
                metrics['Memory Usage'] = 'Error'

            memory_requests = metrics['Memory Requests']
            memory_limits = metrics['Memory Limits']
            memory_usage = metrics['Memory Usage']

            if memory_requests.endswith('Gi'):
                memory_requests = f"{int(memory_requests[:-2]) * 1024}Mi"
                metrics['Memory Requests'] = memory_requests

            if memory_limits.endswith('Gi'):
                memory_limits = f"{int(memory_limits[:-2]) * 1024}Mi"
                metrics['Memory Limits'] = memory_limits

            if memory_usage.endswith('Gi'):
                memory_usage = f"{int(memory_usage[:-2]) * 1024}Mi"
                metrics['Memory Usage'] = memory_usage

            pod_info.append(metrics)

    return pod_info

def generate_csv(metrics_list, node_name):
    keys = ['Namespace', 'Pod Name', 'CPU Requests', 'Memory Requests', 'CPU Limits', 'Memory Limits', 'CPU Usage', 'Memory Usage']
    with open(f'pod_metrics-{node_name}.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(metrics_list)

if __name__ == '__main__':
    node_name = input('Digite o nome do nó do Kubernetes: ')

    pod_info = get_pod_info(node_name)

    generate_csv(pod_info, node_name)

    print('Arquivo CSV gerado com sucesso!')