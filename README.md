I have chosen Project Proposal 1 from [project-proposals.md](project-proposals.md).


## Using MongoDB on Kubernetes to Build and Launch a Containerized Python Application with Flask

### Objective

The purpose of this assignment is to develop a Python application that is scalable and containerized, capable of interacting with a MongoDB database, Flask, and to install it on a Kubernetes cluster.

Students will gain important experience working with database interactions, Kubernetes orchestration, and containerization in a real-world setting with this project. It goes over the basic ideas behind setting up and running containerized apps in a distributed setting.

### Tasks:
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



# to create the cluster 

```
minikube start
kubectl apply -f mongo-statefulset.yaml
kubectl apply -f mongo-service.yaml
MONGOIP=$(minikube service mongodb --url | sed 's,.*/,,')
mongoimport --file=bookstore.json --collection=bookstorecollection --uri=mongodb://192.168.49.2:30524 --jsonArray --db=bookstoredb

```
