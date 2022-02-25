# Setting up your RPi

Please make sure that you have accomplished 1_environment_setup.md before proceeding to this step.<br/>

1. Open Adminer in your browser <br/>

   <img height="350" width="700" src="/tutorial_images/db_1.png"/>

2. Enter your username and password (Example: username=root, password=123456) <br/>

   <img height="400" width="700" src="/tutorial_images/db_2.png"/>

3. Create a MySQL database <br/>

   <img height="400" width="700" src="/tutorial_images/db_3.png"/>

4. Define the database name such as "agriapp_data". Use "utf8_general_ci" as collation. Click Save.<br/>

   <img height="400" width="700" src="/tutorial_images/db_4.png"/>

   \The output should look like this:

   <img height="400" width="700" src="/tutorial_images/db_5.png"/>

5. Next, click Create Table <br/>

   <img height="400" width="700" src="/tutorial_images/db_6.png"/>

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
