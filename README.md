# Music Shop App

## Structure
The project is structured in 3 parts:
- client - user logs in and shops items
- database - storing user accounts and items
- server - administrates database

![diagram](diagram.png "Project diagram")
Docker repo: https://hub.docker.com/r/florinrm/proiect_idp

Git repo: https://github.com/florinrm/ProiectIDP

## Client
How to run client?
1) Build container: `docker build -t client client` (from root folder of the project)
2) Run container: `docker container run -p 8888:5000 client`
3) Access page at http://127.0.0.1:8888/

## Server
How to run server?
1) Build container: `docker build -t server server` (from root folder of the project)
2) Run container: `docker container run -p 5001:5001 client`
3) Access page at http://127.0.0.1:5001/
## Database

## Data monitoring

## Running with docker-compose
```
docker swarm init
docker stack deploy -c .\docker-compose.yml app
docker stack rm app
docker swarm leave --force
```

docker container run -i -p 5001:5001 client
docker container run -p 5000:5000 app
docker container run -p 3306:3306 --env="MYSQL_ROOT_PASSWORD=root" db