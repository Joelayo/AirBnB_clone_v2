#!/usr/bin/env bash
# script to setup web server for the deployment of web_static
sudo apt-get -y update
if [ $(dpkg-query -W -f='${Status}' nginx 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
	sudo apt-get -y install nginx;
fi
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo chown -R ubuntu /data/web_static/releases/test
echo "Holberton School" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
configure="\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo chown -hR ubuntu:ubuntu /data/ 
sudo sed -i "49i\ $configure" /etc/nginx/sites-available/default
sudo service nginx restart
