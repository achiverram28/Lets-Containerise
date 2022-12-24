import os
print("You will be spinning up a nginx server...")
print("Checking the current version of your terraform")
os.system("terraform version")
os.system("terraform plan")
os.system("terraform apply")