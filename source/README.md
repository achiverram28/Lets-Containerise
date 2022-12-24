## Lets-Containerise

Lets-Containerise is a tool , through which you can easily build containerised application and deploy it using kubernetes.By typing just one commmand you you be able to get the template of the application which is containerised.Our idea is to bring in the practise of DevOps and containerisation in a simple way to the people who are new to these , and a time saving task to the cloud native developers .

## What are we focuisng as of now

- As of now , we are planning to containerise a Flask Application . The template contains a hello world Flask Application , which will automatically be containerised using docker and then with help of another command , you can deploy it using kubernetes. Developers can modify their content and go ahead with creating their own images and modify their yaml files for deployment in k8s. The whole idea is to demonstrate how we can containerise any application, with the help of the templates we provide with .
- We have also provided the terraform feature to spin up your nginx server , which is a production based server.

## Prerequisite

- Must have installed Docker Desktop . Otherwise you can visit this [link](https://www.docker.com/products/docker-desktop/) and do the required.
- Must have installed kubectl cli on their system . Otherwise you can visit the [link](https://kubernetes.io/docs/tasks/tools/) and do the needful.
- Enable Kubernetes in you Docker Desktop 
![F3A72418-C240-401D-947C-93725452F762_1_105_c](https://user-images.githubusercontent.com/97288756/209341902-5140e39f-892f-4ab2-9699-3a6d1a18982d.jpeg)
- If you want to use the nginx image built using terraform then you must have installed Terraform in your system. Otherwise you can visit the [link](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) and do the needful.


## Installation
```
// Create a folder for you project in your VsCode

// Move to the repository that you have created

$ cd FolderName

// Clone the repository 

$ git clone https://github.com/achiverram28/Lets-Containerise.git

```

## Usage

```
// If you are a windows user then run this 

$ python3 docker_deploy_win.py

// If you are a mac or linux user the run this file 

$ python3 docker_deploy_linmac.py

// Make sure that you localhost:5000 and localhost:8000 is free
```


![2A53C619-35E3-4318-A0B6-FF2E9306EBBF_1_105_c](https://user-images.githubusercontent.com/97288756/209342415-c815f34e-8d72-4f1a-8ee4-d6272f4c1207.jpeg)

You can see the image the you have created in the docker desktop

![43606211-8EFC-4B55-A1AC-AA8AEA8C2ACF_1_105_c](https://user-images.githubusercontent.com/97288756/209342315-2b800253-682a-4951-a576-c3527bd05775.jpeg)

- You can visit the localhost:5000 to see you application running in the docker conatainer . 

```
// Press Ctrl C to stop the server

// Now move to the directory of the app that you have created 

cd AppName 

// Now to deploy using kubernetes run this command

$ python3 kube_deploy.py 

```

You will see the output as this 

<img width="518" alt="68FFF979-91A8-436A-84F8-B9F60A9DEA2E" src="https://user-images.githubusercontent.com/97288756/209343493-515dc7c7-4f8b-4888-8dfb-dab47d0818b6.png">

Type ```kubectl get pods``` in your terminal after 2 - 3 seconds

You will see the output like this 

![F107EC1B-AA23-463F-8B9F-E26357B96F35_4_5005_c](https://user-images.githubusercontent.com/97288756/209343675-93576865-c770-466e-ad54-df10fc52dbd4.jpeg)

- Then head towards the localhost:8000 , there you go , you have deployed your application using kubernetes 😀.

- Modify the template according your application , you can also mody the Dockerfile and deployment.yaml to modify your development.

- You can delete the kubernetes cluster you created using ```kubectl delete deployment hello-python```. Here I have named the deployment as hello-python , you can modify it . You can delete the images and conatiners in your Docker desktop and run your own images.

## Terraform Part

- This feature is automatically installed during you installation. If you want to integrate your flask application with nginx server, then follow these procedures .

```
// Move to the named Directory which you have created when asked for entering your app name

$ cd appName

// Move to the Terraform_Nginx directory 

$ cd Terraform_Nginx

// If you are a mac or linux user then perform the below mentioned.

$ python3 terraform_deploy.py

// If you are windows user , then go ahead with this

$ python3 Terraform_deploy.py

```
- You can see the following out like this : 
![4896CEC4-BEF7-424C-A160-69596B925FD3_1_105_c](https://user-images.githubusercontent.com/97288756/209433265-f9432b0a-6823-4b15-abe9-49de5fe4a8a6.jpeg)

- When you come across this permission , type in yes

![D3D3F636-1A56-498A-86BA-2A486E5D026B_4_5005_c](https://user-images.githubusercontent.com/97288756/209433294-f1251bd7-acd8-4ba9-b895-5d2d76bf250d.jpeg)

- Finally if you head towards localhost:7500 , you can view your nginx server running. You can later use this nginx image and use it as a node in kubernetes and deploy you application there.

![5E215204-4AA3-4488-901E-5ECB0DEE6BD7_1_105_c](https://user-images.githubusercontent.com/97288756/209433331-ceff4678-b223-44df-887a-7c3dc0054288.jpeg)



## Future Releases

- Conatinerise the Django App
- Conatinerise other frameworks
- Focus on CI/CD pipeline using Jenkins or Github Actions

## Contact 

Email => achiverram28@gmail.com




