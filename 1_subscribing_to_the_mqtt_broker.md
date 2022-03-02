# Running an MQTT subscriber for collecting data

We have already cloned the github repository that contains the codes for this part. Open File explorer (the second icon found on the lower left of your VM). Open the <b>agriapp_iot</b> folder.

1. Right click on the file <b>agriapp_sensor_subscriber.py</b> and click Thonny Python IDE <br/>
   This opens the file in a Python programming IDE called Thonny. </br>

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
