import os
dir_1=os.getcwd()
app_name = input("Enter your app name: ")
cmd_1="mkdir {}".format(app_name)
os.system(cmd_1)
print("Completed creating the {} directory .....".format(app_name))
curr_dir=os.getcwd()
os.chdir("{}/{}".format(curr_dir,app_name))
cmd_2="mkdir app"
os.system(cmd_2)
print("Completed creating the app directory .....")
cmd_2_1="mkdir templates"
os.system(cmd_2_1)
print("Completed creating the templates directory .....")
curr_dir_app=os.getcwd()
cmd_3="copy \"{}\Tool\Docker\Dockerfile\" \"{}\"".format(dir_1,curr_dir_app)
os.system(cmd_3)
print("Completed creating the Dockerfile .....")
cmd_4="copy \"{}\Tool\Kubernetes\deployment.yaml\" \"{}\"".format(dir_1,curr_dir_app)
os.system(cmd_4)
print("Completed creating the deployment.yaml .....")
cmd_6_0="copy \"{}\Tool\Python\kube_deploy.py\" \"{}\"".format(dir_1,curr_dir_app)
os.system(cmd_6_0)
print("Creating kube_deploy.py .... ")
os.system("mkdir Terraform_Nginx")
print("Created the Terraform_Nginx Directory")
os.chdir("{}/{}/Terraform_Nginx".format(dir_1,app_name))
cmd_6_1="copy \"{}\Tool\Terraform_Win\main.tf\" \"{}\"".format(dir_1,curr_dir_app)
print("Created the main.tf")
os.system(cmd_6_1)
cmd_6_2="copy \"{}\Tool\Terraform_Win\Terraform_deploy.py\" \"{}\"".format(dir_1,curr_dir_app)
os.system(cmd_6_2)
print("Created the terraform_deploy.py")
os.chdir("{}/{}/app".format(dir_1,app_name))
cmd_5="copy \"{}\Tool\Python\main.py\" \"{}\"".format(dir_1,os.getcwd())
os.system(cmd_5)
print("Completed creating the main.py .....")
cmd_6="copy null > requirements.txt"
os.system(cmd_6)
print("Completed creating the requirements.txt .....")
print("Successfully completed your project template...😃")
new_dir="{}/{}".format(curr_dir,app_name)
cmd_7="docker build -f {}/Dockerfile -t hello-python:latest {}".format(new_dir,os.getcwd())
os.system(cmd_7)
print("Building the docker image....")
cmd_8="docker run -p 5000:5000 hello-python"
os.system(cmd_8)
