[Create Network to connect each containers]
sudo docker network create --gateway 172.33.0.1 --subnet 172.33.0.0/16 broker 

[start nginx - tomcat - mysql + python CLI]
sudo docker-compose up -d