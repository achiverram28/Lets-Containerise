import os
print("Checking your kubectl version using yaml...")
os.system("kubectl version --client --output=yaml")
print("Creating the deployment .....")
os.system("kubectl apply -f ./deployment.yaml")
print("Checking the pods...")
os.system("kubectl get pods")
print("Head towards http://localhost:8000")
