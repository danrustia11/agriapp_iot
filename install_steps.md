# Setting up your RPi

The following steps are used to install the following:<br/>
Apache (Web server)<br/>
MySQL (Database)<br/>
phpMyAdmin (Database web interface)<br/>
Grafana (Data visualization platform)<br/>

1. Install Apache: <br/>

   ```bash
   sudo apt-get update                                  # updates RPi
   sudo apt-get install apache2                         # Installs Apache2
   sudo usermod -a -G www-data pi                       # Adds a new user to access the apache directory
   sudo chown -R -f www-data:www-data /var/www/html     # Allow acces to apache directory
   ```

2. Install MySQL: <br/>

   ```bash
   sudo apt-get install mariadb-server  # Installs MySQL
   sudo mysql_secure_installation
   ```

   <img height="700" width="500" src="/tutorial_images/mysql.png"/>

3. Configure MySQL: <br/>

   ```bash
   sudo mysql -u root -p    # Logs in to MySQL environment
   GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' IDENTIFIED BY 'password' WITH GRANT OPTION;
   ```

   <img height="200" width="650" src="/tutorial_images/mysql_2.png"/>

   \*Replace username and password with the ones defined in the setup.
   Exit the MySQL environment by CTRL+C.

4. Install phpMyAdmin <br/>

   ```bash
   sudo apt-get install phpmyadmin  # Installs phpmyadmin
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

    <img height="400" width="700" src="/tutorial_images/apache.png"/>

   Press CTRL+O then ENTER to save the file.
   Restart apache to apply the changes.

   ```bash
   sudo service apache2 restart
   ```

6. Install Grafana
   ```bash
   wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
   echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
   sudo apt-get update
   sudo apt-get install grafana
   sudo /bin/systemctl enable grafana-server
   sudo /bin/systemctl start grafana-server
   ```
