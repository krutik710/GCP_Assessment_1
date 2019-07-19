#! /bin/bash
apt-get update 
apt-get install -y apache2
rm /var/www/html/index.html
echo "<h1>This is running from $HOSTNAME</h1>" >> /var/www/html/index.html
