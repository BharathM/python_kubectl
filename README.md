# python_kubectl
Run the same commands on multiple pods (Filter the PODs by name)

This python program run the following command and get the list of all the available pods in the namespace.

kubectl get pods -o wide

From this list, it will filter all the PODs that have the name "server" and run the following command on all the pods

kubectl exec POD NAME -- curl localhost:8081/status
