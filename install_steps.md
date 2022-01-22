# Environmental setup

1. Install Apache:
   sudo apt-get update
   sudo apt-get install apache2 -y
   sudo usermod -a -G www-data pi
   sudo chown -R -f www-data:www-data /var/www/html
