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


# Steps to run the project

First of all you need a kubernetes cluster. I have used minikube for this project. I also installed mongo client on my machine to test stuff and feed the test data to the mongo instance.



## Step 1: Setup the kubernetes cluster
Lets start the minikube cluster

```
minikube start
```

After this lets look at the status of the cluster

```
kubectl get nodes
```

Output should be something like this

```
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   22s   v1.28.3
```

## Step 2: Create the mongo statefulset

Now lets create the mongo statefulset. This will create a mongo instance with 1 replica. We want 2 things from this mongo database 1 feed the data to the python app and 2 to expose the mongo instance to outside of the kubernetes cluster. So we will create a service that uses the mongo statefulset as its backend.

```
kubectl apply -f mongo-statefulset.yaml
```

Lets check the status of the kubernetes:

```
kubectl get all
```

Output should be something like this:

```
NAME            READY   STATUS              RESTARTS   AGE
pod/mongodb-0   0/1     ContainerCreating   0          4s

NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   3m30s

NAME                       READY   AGE
statefulset.apps/mongodb   0/1     4s
```

Lets wait until the mongodb-0 pod is ready.

```
NAME            READY   STATUS    RESTARTS   AGE
pod/mongodb-0   1/1     Running   0          2m4s

NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   5m30s

NAME                       READY   AGE
statefulset.apps/mongodb   1/1     2m4s
```

Thats better.

## Step 3: Create the mongo service

Now lets create the service for the mongo statefulset. This will expose the mongo instance to outside of the kubernetes cluster.

```
kubectl apply -f mongo-service.yaml
```

Lets check the status of the kubernetes (from now on I will not show the output of this command):

```
NAME            READY   STATUS    RESTARTS   AGE
pod/mongodb-0   1/1     Running   0          3m24s

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)           AGE
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP           6m50s
service/mongodb      LoadBalancer   10.98.168.165   <pending>     27017:31692/TCP   2s

NAME                       READY   AGE
statefulset.apps/mongodb   1/1     3m24s
```

## Step 4: Import the data to the mongo instance

Now lets import the data to the mongo instance. For this we need to get the mongo uri. We can get it by running the following command:

```
export MONGO_URI=mongodb://$(minikube service mongodb --url | sed 's,.*/,,')
mongoimport --file=bookstore.json --collection=bookstorecollection --uri=$MONGO_URI --jsonArray --db=bookstoredatabase
```

## Step 4.1 (optional): Check the data in the mongo instance

You can actually access the mongo instance from your machine by running the following command:

```
mongosh $MONOGO_URI
```

And once inside:

```
show dbs
```

Output should be something like this:

```
admin              32.00 KiB
bookstoredatabase  32.00 KiB
config             12.00 KiB
local              32.00 KiB
```

## Step 5: Create the flask deployment

Now lets create the flask deployment. This will create a flask instance with 1 replica. The docker image of the flask application will be pulled from [my docker hub repository](https://hub.docker.com/r/osbm/ain3003-flask-application). The docker image is created from the Dockerfile in the flask-application directory. So this may take some time to pull the image.

```
kubectl apply -f flask-deployment.yaml
```

Lets check the status of the kubernetes:

```
NAME                             READY   STATUS    RESTARTS   AGE
pod/flask-app-76966bdd64-gmxmx   1/1     Running   0          39s
pod/mongodb-0                    1/1     Running   0          14m

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)           AGE
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP           17m
service/mongodb      LoadBalancer   10.98.168.165   <pending>     27017:31692/TCP   10m

NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/flask-app   1/1     1            1           40s

NAME                                   DESIRED   CURRENT   READY   AGE
replicaset.apps/flask-app-76966bdd64   1         1         1       39s

NAME                       READY   AGE
statefulset.apps/mongodb   1/1     14m
```


## Step 6: Create the flask service

Now lets create the flask service. This will expose the flask instance to outside of the kubernetes cluster.

```
kubectl apply -f flask-service.yaml
```

Lets check the status of the kubernetes:

```
NAME                             READY   STATUS    RESTARTS   AGE
pod/flask-app-76966bdd64-gmxmx   1/1     Running   0          3m47s
pod/mongodb-0                    1/1     Running   0          17m

NAME                 TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)           AGE
service/flask        LoadBalancer   10.109.40.227   <pending>     5000:30669/TCP    6s
service/kubernetes   ClusterIP      10.96.0.1       <none>        443/TCP           20m
service/mongodb      LoadBalancer   10.98.168.165   <pending>     27017:31692/TCP   14m

NAME                        READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/flask-app   1/1     1            1           3m48s

NAME                                   DESIRED   CURRENT   READY   AGE
replicaset.apps/flask-app-76966bdd64   1         1         1       3m47s

NAME                       READY   AGE
statefulset.apps/mongodb   1/1     17m
```


## Step 7: Test the flask application

Now lets test the flask application. For this we need to get the flask uri. We can get it by running the following command:

```
minikube service flask
```
