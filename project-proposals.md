# Project Proposal 1

Project Title: Using MongoDB on Kubernetes to Build and Launch a Containerized Python Application with Flask

Objective: The purpose of this assignment is to develop a Python application that is scalable and containerized, capable of interacting with a MongoDB database, Flask, and to install it on a Kubernetes cluster.

Students will gain important experience working with database interactions, Kubernetes orchestration, and containerization in a real-world setting with this project. It goes over the basic ideas behind setting up and running containerized apps in a distributed setting.

## Tasks:
- Task-1: Construct MongoDB:
    - Use a Kubernetes StatefulSet to deploy a MongoDB instance.
    - To expose the MongoDB instance, create a Kubernetes service.
    - Use BOOKSTORE database from our MongoDb Classes
- Task-2: Develop Python Application: Create a Python script that carries out CRUD (Create, Read, Update, Delete) actions by connecting to the MongoDB instance.
    - Employ a Python driver for MongoDB (like PyMongo) to communicate with the database.
    - Use Flask tools to ensure a RESTful application
    - Use Docker to containerize the Python program.
- Task-3: Kubernetes Deployment:
    - Establish a Python application Kubernetes deployment.
    - For configuration, use Kubernetes ConfigMaps or environment variables.
- Task-4: Service Discovery: Using Kubernetes Services, implement service discovery between the Python application and MongoDB.
    - Verify that the MongoDB instance can be dynamically found and connected to by the Python program.
- Task-5: Documentation:
    - Clearly explain how to install and use the complete system in your documentation.
    - Provide guidance on how to launch the Python application on Kubernetes, build and push the Docker image, and launch the MongoDB instance.


## Submission
The following must be turned in by students:
- Entire source code for the Python program.
- YAML files pertaining to StatefulSet, Deployment, and other Kubernetes resource types.
- Explanations and detailed instructions included in the documentation.

## Evaluation Standards
- Proper implementation of CRUD operations in the Python application.
- The Python + Flask application was successfully deployed on Kubernetes.
- Proper MongoDB setup and configuration on Kubernetes.
- Clear and well-organized documentation.


# Project Proposal 2

Project Title: Building and Deploying a Containerized Python Application with Flask and MongoDB on Azure Kubernetes Service (AKS)
Objective: The goal of this assignment is to create a scalable and containerized Python and Flask application that interacts with a MongoDB database and deploy the application on Azure Kubernetes Service (AKS).

Through this project, students will gain hands-on experience using Azure Kubernetes Service and other Azure services to deploy cloud-native apps. It goes over the basic ideas of database interactions in a cloud environment, container orchestration, and cloud computing.
Tasks:
- Task-1: Setup MongoDB on Azure:
    - Deploy a MongoDB instance on Azure using Azure Cosmos DB with the MongoDB API.
    - Configure necessary network settings and authentication
    - Use BOOKSTORE database from our MongoDb Classes.
- Task-2: Python Application:
    - Write a Python script that connects to the Azure Cosmos DB MongoDB instance and performs CRUD operations.
    - Use the PyMongo driver for Python to interact with the database.
    - Use Flask to ensure a RESTful application
    - Containerize the Python application using Docker.
- Task-3: Azure Kubernetes Service (AKS):
    - Create an AKS cluster on Microsoft Azure.
    - Deploy MongoDB on AKS.
    - Configure a Kubernetes Service to expose the MongoDB instance.
- Task-4: Python Application Deployment:
    - Create a Kubernetes Deployment for the Python application on AKS.
    - Use Flask to ensure a RESTful application
    - Utilize Azure Container Registry (ACR) to store the Docker image.
    - Configure the Deployment to use multiple replicas for scalability.
    - Use Azure Kubernetes ConfigMaps for configuration.
- Task-5: Service Discovery and Networking:
    - Implement service discovery between the Python application and MongoDB on AKS.
    - Utilize Azure Virtual Network and Network Policies for secure communication.
- Task-6: Documentation:
    - Provide clear documentation on how to set up and run the entire system on Azure.
    - Include instructions for deploying MongoDB on Azure Cosmos DB, building and pushing the
    - Docker image to ACR and deploying the Python application on AKS.


## Submission

- Entire source code for the Python application.
- YAML files for Kubernetes resources (Deployment, Service, StatefulSet, etc.).
- Documentation with step-by-step instructions and explanations for deploying on Azure.


## Grading Criteria

- Proper implementation of CRUD operations in the Python application.
- Correct deployment and configuration of MongoDB on Azure Cosmos DB.
- The Python + Flask application was successfully deployed on Kubernetes.
- Effective use of Azure services for container registry and logging.
- Clear and well-organized documentation.

