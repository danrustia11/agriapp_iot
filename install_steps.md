# Environmental setup

1. Install Apache:
   sudo apt-get update <br/>
   sudo apt-get install apache2 -y <br/>
   sudo usermod -a -G www-data pi <br/>
   sudo chown -R -f www-data:www-data /var/www/html <br/>
