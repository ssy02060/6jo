### [ If you didn't clone this repositroy... ]

```bash
git clone https://github.com/ssy02060/6jo.git
```

### [ Remove ALL CONTAINERS AND IMAGES ]

```bash
sudo docker rm -f $(sudo docker ps -aq)
sudo docker rmi $(sudo docker images -q)
```

### [ Create Network to connect each containers ]

```bash
sudo docker network create --gateway 172.33.0.1 --subnet 172.33.0.0/16 broker 
```

### [ Create and start containers : nginx - tomcat - mysql + python CLI ]

```bash
sudo docker-compose up -d
```

### [ Start user management system in python cli ]
```bash
sudo docker start -i python-cli
```
