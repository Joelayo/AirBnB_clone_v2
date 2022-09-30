#!/usr/bin/env bash
# Installs, configures, and starts the web server
if [[ "$(which nginx | grep -c nginx)" == '0' ]]; then
	sudo apt-get update
	sudo apt-get -y install nginx
fi
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo chown -R ubuntu /data/web_static/releases/test
echo "Welcome to AirBnB!" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
configure="\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo chown -hR ubuntu:ubuntu /data/ 
sudo sed -i "49i\ $configure" /etc/nginx/sites-available/default
sudo service nginx restart
sudo service nginx reload