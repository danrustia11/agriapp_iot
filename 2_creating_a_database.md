# Setting up your RPi

Please make sure that you have accomplished 1_environment_setup.md before proceeding to this step.<br/>

1. Open Adminer in your browser <br/>

   <img height="400" width="700" src="/tutorial_images/db_1.png"/>

2. Enter your username and password (Example: username=root, password=123456) <br/>

   <img height="400" width="700" src="/tutorial_images/db_2.png"/>

3. Create a MySQL database <br/>

   <img height="400" width="700" src="/tutorial_images/db_3.png"/>

4. Define the database name such as "agriapp_data". Use "utf8_general_ci" as collation.<br/>

   <img height="400" width="700" src="/tutorial_images/db_4.png"/>

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
