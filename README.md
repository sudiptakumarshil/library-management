# Create a new Django project. Access the running container:
    $ docker-compose run web django-admin startproject myproject .

# Create a new app:
    $ docker-compose run web django-admin startapp myapp

# Run the project:
    $ docker-compose build
    $ docker-compose up -d

# Restart Docker Containers:
    $ docker-compose down
    $ docker-compose up -d
    
# Check all running containers:
    $ docker ps

# Check the error log:
    $ docker logs 402a0f984fbf <- container ID
