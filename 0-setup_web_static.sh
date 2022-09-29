#!/usr/bin/env bash
# script to setup web server for the deployment of web_static
sudo apt-get -y update
if [ $(dpkg-query -W -f='${Status}' nginx 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
	sudo apt-get -y install nginx;
fi
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "Coding School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# configure="/location \/ /{:a; N; /\}/!ba; a\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo chown -hR ubuntu:ubuntu /data/ 
sudo sed -i '/location \/ /{:a; N; /\}/!ba; a\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' -e '}' /etc/nginx/sites-available/default
sudo service nginx restart
