# Setting up your RPi

1. Install Apache: <br/>

   ```bash
   sudo apt-get update
   sudo apt-get install apache2 -y
   sudo usermod -a -G www-data pi
   sudo chown -R -f www-data:www-data /var/www/html
   ```

2. Install MySQL: <br/>

   ```bash
   sudo apt-get install mariadb-server
   sudo mysql_secure_installation
   ```

3. Test MySQL: <br/>

   ```bash
   sudo mysql -u root -p
   GRANT ALL PRIVILEGES ON _._ TO 'username'@'localhost' IDENTIFIED BY 'password' WITH GRANT OPTION;
   ```
