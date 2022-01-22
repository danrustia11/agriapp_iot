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

   <img height="700" width="500" src="/tutorial_images/mysql.png"/>

3. Configure MySQL: <br/>

   ```bash
   sudo mysql -u root -p
   GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' IDENTIFIED BY 'password' WITH GRANT OPTION;
   ```

   <img height="200" width="500" src="/tutorial_images/mysql_2.png"/>

   Exit the MySQL environment by CTRL+C.

4. Install phpMyAdmin <br/>

   ```bash
   sudo apt-get install phpmyadmin
   ```

    <img height="700" width="600" src="/tutorial_images/phpmyadmin.png"/>

5. Configure apache by opening and editing the apache2.conf<br/>

   ```bash
   sudo nano /etc/apache2/apache2.conf
   ```

   Add this line at the bottom of the apache2.conf

   ```bash
   Include /etc/phpmyadmin/apache.conf
   ```

   Press CTRL+O then ENTER to save the file.
