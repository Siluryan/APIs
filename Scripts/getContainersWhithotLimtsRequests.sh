#!/bin/bash

namespaces=$(kubectl get namespaces -o jsonpath='{.items[*].metadata.name}')

csv_file="containers_without_limits_requests.csv"

echo "Namespace,Pod,Container" > "$csv_file"

for namespace in $namespaces; do
  pods=$(kubectl get pods -n "$namespace" -o jsonpath='{.items[*].metadata.name}')

  for pod in $pods; do
    containers=$(kubectl get pods "$pod" -n "$namespace" -o jsonpath='{.spec.containers[*].name}')

    for container in $containers; do
      limits=$(kubectl get pod "$pod" -n "$namespace" -o jsonpath="{.spec.containers[?(@.name == '$container')].resources.limits}")
      requests=$(kubectl get pod "$pod" -n "$namespace" -o jsonpath="{.spec.containers[?(@.name == '$container')].resources.requests}")

      if [ -z "$limits" ] && [ -z "$requests" ]; then
        echo "$namespace,$pod,$container" >> "$csv_file"
      fi
    done
  done
done

echo "A listagem dos containers sem limits e requests foi salva em $csv_file."
