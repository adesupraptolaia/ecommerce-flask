#!/bin/bash

sudo docker stop flask-travis
sudo docker rm flask-travis
sudo docker rmi adesupraptolaia/flask-travis
sudo docker run -d --name flask-travis -p 5000:5000 adesupraptolaia/flask-travis:latest