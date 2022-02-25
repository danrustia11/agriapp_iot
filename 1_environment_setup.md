# Setting up your RPi

The following steps are used to install the following:<br/>
Apache (Web server)<br/>
MySQL (Database)<br/>
Adminer (Database web interface)<br/>
Grafana (Data visualization platform)<br/>
<br/>
TIP: You can copy each line to the terminal by CTRL+SHIFT+V<br/>

1. Install Apache: <br/>

   ```bash
   sudo apt-get update                                  # Updates RPi
   sudo apt-get install apache2 -y                      # Installs Apache2
   sudo usermod -a -G www-data pi                       # Adds a new user to access the apache directory
   sudo chown -R -f www-data:www-data /var/www/html     # Allow access to apache directory
   ```

2. Install MySQL: <br/>

   ```bash
   sudo apt-get install mariadb-server -y               # Installs MySQL
   sudo mysql_secure_installation
   ```

   <img height="700" width="500" src="/tutorial_images/mysql.png"/>

3. Configure MySQL: <br/>

   ```bash
   sudo mysql -u root -p    # Logs in to MySQL environment
   GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED BY '123456' WITH GRANT OPTION;
   ```

   <img height="200" width="650" src="/tutorial_images/mysql_2.png"/>

   \*root is the username, while 123456 is the password
   Exit the MySQL environment by CTRL+C.

4. Install Adminer <br/>

   ```bash
   sudo apt-get install php-mysql                                                   # Installs php-mysql plugin for enabling adminer
   sudo mkdir /usr/share/adminer                                                    # Creates a new directory for adminer
   sudo wget -O /usr/share/adminer/index.php http://www.adminer.org/latest-en.php   # Downloads the latest version of adminer
   ```

5. Add Adminer to Apache <br/>

   ```bash
   sudo nano /etc/apache2/conf-available/adminer.conf    # Opens adminer.conf using nano text editor
   ```

   Copy and paste these lines to the opened file:

   ```bash
   Alias /adminer /usr/share/adminer

   <Directory /usr/share/adminer>
    Options Indexes FollowSymLinks
    AllowOverride None
    Require all granted
   </Directory>
   ```

    <img height="500" width="700" src="/tutorial_images/adminer_configuration.png"/>

   Press CTRL+O then ENTER to save the file.
   Restart apache to apply the changes.

   ```bash
   sudo a2enconf adminer.conf                            # Enables adminer
   sudo service apache2 restart                          # Restarts apache service
   ```

   Test your installation by opening Chromium in your RPi then enter "http://localhost/adminer/". It should open a page that looks like this:

   <img height="400" width="800" src="/tutorial_images/adminer.png"/>

6. Install Grafana

   ```bash
   wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -                                            # Adds Grafana channel for updating
   echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
   sudo apt-get update
   sudo apt-get install grafana=6.7.6 -y              # Install Grafana
   sudo /bin/systemctl enable grafana-server          # Enables Grafana (so it will run during start up)
   sudo /bin/systemctl start grafana-server           # Starts Grafana service
   ```

   Test your installations by opening Chromium in your RPi then enter "http://localhost:3000". It should open a page that looks like this:

   <img height="400" width="600" src="/tutorial_images/grafana.png"/>
