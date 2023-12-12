#!/bin/bash

# Author: Dipali Dhanwade

# Description: 

setVariables()
{
    #defining directory path.
    # path="/home/ubuntu/Node-Project"
    path="/home/dipali_dhanwade/shopping-project"
    
    #defining nginx path
    nginx_path="/etc/nginx/sites-enabled"

}

getVariables()
{
    echo "Path:$path"
    echo "Nginx Path:$nginx_path"

}


setVariables

#Install Nginx Server
sudo apt-get install nginx -y >/dev/null || { echo "Failed to Install Nginx Server"; exit 1; }

#Configuring Nginx Server:
sudo rm "$nginx_path/default" || echo "Default Config File Not Found"
cd "$path/Execution-Script/"
sudo cp "default" "$nginx_path/"
sudo systemctl restart nginx

echo "*** Successfully Configured Nginx ***"

cd

sudo apt-get install docker -y >/dev/null && echo "** Successfully Installed Docker **" || { echo "Failed to Install Docker"; exit 1; }
sudo apt-get install docker-compose -y >/dev/null && echo "** Successfully Installed Docker-Compose **" || { echo "Failed to Install Docker-Copmose"; exit 1; }


cd "$path"

sudo docker-compose down && echo "Docker Is Down Now" || echo "Docker Already Down"

#sudo docker rm shopping-project_frontend_1
#sudo docker rm shopping-project_backend_1

sudo docker rmi shopping-project_frontend || echo "Error deleting frontend image"
sudo docker rmi shopping-project_backend || echo "Error deleting backend image"

sudo docker-compose up -d || echo "error in compose file"



#-----------------------------------------------------------------------------------------------------------------------------------------
# backend_container_id=$(sudo docker ps -a | grep backend | awk '{print $1}')
# sudo docker rm $backend_container_id 2>/dev/null || echo "Backend Container Not Found"

# frontend_container_id=$(sudo docker ps -a | grep frontend | awk '{print $1}')
# sudo docker rm $frontend_container_id 2>/dev/null || echo "Frontend Container Not Found"

# backend_image_id=$(sudo docker images | grep backend | awk '{print $3}')
# sudo docker rmi $backend_image_id  2>/dev/null || echo "Backend Image Not Found"

# frontend_image_id=$(sudo docker images | grep frontend | awk '{print $3}')
# sudo docker rmi $frontend_image_id 2>/dev/null || echo "Frontend Image Not Found"
#-----------------------------------------------------------------------------------------------------------------------------------------
