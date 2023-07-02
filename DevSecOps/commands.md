docker run [image-name]
docker run [image-name] [command]
ex- docker run busybox ping google.com
ex- docker run -it busybox sh

docker run [docker-id]/[image-name] 
docker run -p 8080:8080 [docker-id]/[image-name] 

# Run in background 
docker run -d redis

docker ps   
docker ps --all

docker create [image-name]
docker start -a [image-id]

docker build .

# Tagging an Image
  docker build -t [docker-id]/[image-name]:version .
  docker build -t e880613/postgres-notes:v1 .

  

# Get logs from a container 
docker logs [container-id] 

# stop
docket stop [container-id]

# kill
docket kill [container-id]

# Execute an additional command in a container
docker exec -it [container-id] [command]

# Note: 
  Option -a docker attached to the container and watch the output and print in the terminal 

docker system prune

This will remove:
- all stopped containers
- all networks not used by at least one container
- all dangling images
- all build cache

# Docker Compose 
  - Separate CLI that gets installed along with Docker
  - Used to start up multiple DOcker containers at the same time
  - Automates some of the long-winded arguments we were passing to 'docker-run'

# docker-compose.yml
  Contains all the options we would normally pass to docker-cli

  docker CLI commands -> docker-compose.yml -> docker-compose CLI

# docker-compose commands
docker-compose up -d
docker-compose down
docker-compose --build

# Restart Policies
  - "no"
  - always
  - on-failure
  - unless-stopped 