#!/bin/bash

# Author: Dipali Dhanwade

# Description: 

setVariables()
{
    #defining directory path.
    path="/home/dipali_dhanwade/StaticIP-MultiVM-DockerProject"

}

getVariables()
{
    echo "Path:$path"

}


setVariables

cd

sudo apt-get install docker -y >/dev/null && echo "** Successfully Installed Docker **" || { echo "Failed to Install Docker"; exit 1; }
sudo apt-get install docker-compose -y >/dev/null && echo "** Successfully Installed Docker-Compose **" || { echo "Failed to Install Docker-Copmose"; exit 1; }


cd "$path"

sudo docker-compose down && echo "Docker Is Down Now" || echo "Docker Already Down"

sudo docker rmi staticip-multivm-dockerproject_backend || echo "Error deleting backend image"

sudo docker-compose up -d || echo "error in compose file"

