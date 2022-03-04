# Storing data to the MySQL database

Before proceeding to this step, please make sure that you have successfully created a MySQL database as accomplished by following 3_creating_a_database.md. <br/> 

1. Open the <b>agriapp_iot</b> folder. Right click on the file <b>agriapp_sensor_subscriber_mysql.py</b> and click Thonny Python Ide <br/>
   This is the same program with the one opened earlier (agriapp_sensor_subscriber.py) but with the MySQL connections and queries included.  </br>

   <img height="500" width="700" src="/tutorial_images/mqtt_1.png"/>

2. Listen to the code explanation provided by your instructor (or if you are doing this after the workshop, please rewatch the video) <br/>

3. Change the target_node variable depending on which node's data you want to collect <br/>

   <img height="500" width="700" src="/tutorial_images/mqtt_2.png"/>

4. Run the program by clicking Run, as found at the top of the IDE <br/>
   The output should look like this: </br>

   <img height="500" width="700" src="/tutorial_images/mqtt_3.png"/>

5. Go back to your web browser and open adminer (http://localhost/adminer). <br/>
   a. Login using your previously defined credentials. </br>

   <img height="500" width="700" src="/tutorial_images/mqtt_4.png"/>

   b. Click the database name (agriapp_data) </br>

   <img height="500" width="700" src="/tutorial_images/mqtt_5.png"/>

   c. Click the table name (sensor_data) </br>

   <img height="500" width="700" src="/tutorial_images/mqtt_6.png"/>

   d. Click Select data </br>

   <img height="500" width="700" src="/tutorial_images/mqtt_7.png"/>

   e. Watch as your data gets updated (you need to refresh your browser to see the changes) </br>

   <img height="500" width="700" src="/tutorial_images/mqtt_8.png"/>
