### [ If you didn't clone this repositroy... ]
- git clone https://github.com/ssy02060/6jo.git

### [ Remove ALL CONTAINERS AND IMAGES ]
- sudo docker rm -f $(sudo docker ps -aq)
- sudo docker rmi $(sudo docker images -q)

### [ Create Network to connect each containers ]
- sudo docker network create --gateway 172.33.0.1 --subnet 172.33.0.0/16 broker 

### [ Create and start containers : nginx - tomcat - mysql + python CLI ]
- sudo docker-compose up -d

### [ Start user management system in python cli ]
- sudo docker run -it --network=broker python-cli
