# Creating a Grafana dashboard

1. Open your web browser and enter http://localhost:3000. If this is your first time logging into Grafana, enter the default username=admin and password=admin </br>

   <img height="500" width="700" src="/tutorial_images/grafana_1.png"/>

2. The web page will ask you about a new password for your Grafana. Preferably, set the password as "123456" so we can assist you easily if you have a problem </br>

   <img height="500" width="700" src="/tutorial_images/grafana_2.png"/>

3. First, click Add data source. In this context, data source means a database such as MySQL. </br>

   <img height="500" width="700" src="/tutorial_images/grafana_3.png"/>

4. Scroll down and find MySQL, then click Select </br>

   <img height="500" width="700" src="/tutorial_images/grafana_4.png"/>

5. Setup the data source by: </br>
   a. Set host = localhost:3306 </br>
   (3306 is the default port of MySQL)
   b. Set database = agriapp_data </br>
   c. Set user = root </br>
   d. Set password = 123456 </br>

   <img height="500" width="700" src="/tutorial_images/grafana_5.png"/>

6. Save and test the data source </br>

   <img height="500" width="700" src="/tutorial_images/grafana_6.png"/>

7. If it shows "Database Connection OK", then the data source was properly connected to Grafana </br>
   Click the Grafana icon found on the upper left of the interface to go back to the Home page </br>

   <img height="500" width="700" src="/tutorial_images/grafana_7.png"/>

8. Create a new dashboard by clicking New dashboard </br>

   <img height="500" width="700" src="/tutorial_images/grafana_8.png"/>

9. Click Add Query </br>

   <img height="500" width="700" src="/tutorial_images/grafana_9.png"/>

10. In the Add Query page, first click on the Metric column and select TYPE </br>

   <img height="500" width="700" src="/tutorial_images/grafana_10.png"/>

11. Click the "Macro: $\_timeFilter" and click Remove </br>

   <img height="500" width="700" src="/tutorial_images/grafana_11.png"/>

12. Click the (+) icon found on the WHERE </br>

   <img height="500" width="700" src="/tutorial_images/grafana_12.png"/>

13. Enter "TYPE='T'" </br>
    (This allows you to select which data you want to get such as T, P, or H) </br>

   <img height="500" width="700" src="/tutorial_images/grafana_13.png"/>

14. Click the Time column and select TIMESTAMP </br>

   <img height="500" width="700" src="/tutorial_images/grafana_14.png"/>

15. Click the "Last 6 hours" found at the upper right of the web page and select Last 5 minutes </br>

   <img height="500" width="700" src="/tutorial_images/grafana_15.png"/>

16. Finally, you will be able to see your data drawn using Grafana. Go back to your dashboard by clicking the "<-" icon </br>

   <img height="500" width="700" src="/tutorial_images/grafana_16.png"/>

17. Congratulations on making your first Grafana dashboard! </br>

   <img height="500" width="700" src="/tutorial_images/grafana_17.png"/>
