#!/bin/bash
echo Nome do pod:
read pod
echo Namespace:
read ns

kubectl get pods $pod -n $ns --no-headers -o custom-columns=":metadata.name, :status.phase"
