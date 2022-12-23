## Lets-Containerise

Lets-Containerise is a tool , through which you can easily build containerised application and deploy it using kubernetes.By typing just one commmand you you be able to get the template of the application which is containerised.Our idea is to bring in the practise of DevOps and containerisation in a simple way to the people who are new to these , and a time saving task to the cloud native developers .

## What are we focuisng as of now

As of now , we are planning to containerise a Flask Application . The template contains a hello world Flask Application , which will automatically be containerised using docker and then with help of another command , you can deploy it using kubernetes. Developers can modify their content and go ahead with creating their own images and modify their yaml files for deployment in k8s. The whole idea is to demonstrate how we can containerise any application, with the help of the templates we provide with .

## Prerequisite

- Must have installed Docker Desktop . Otherwise you can visit this [link](https://www.docker.com/products/docker-desktop/) and do the required.
- Must have installed kubectl cli on their system . Otherwise you can visit the [link](https://kubernetes.io/docs/tasks/tools/) and do the needful.
- Enable Kubernetes in you Docker Desktop 
![F3A72418-C240-401D-947C-93725452F762_1_105_c](https://user-images.githubusercontent.com/97288756/209341902-5140e39f-892f-4ab2-9699-3a6d1a18982d.jpeg)


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
```
