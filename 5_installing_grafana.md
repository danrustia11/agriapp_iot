# Installing Grafana



To install Grafana, open the terminal and enter the following commands. <br/>
<br/>
TIP: You can copy each line to the terminal by CTRL+SHIFT+V<br/>

```bash
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -                 # Adds Grafana channel for updating
echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
sudo apt-get update
sudo apt-get install grafana=6.7.6 -y              # Install Grafana
sudo /bin/systemctl enable grafana-server          # Enables Grafana (so it will run during start up)
sudo /bin/systemctl start grafana-server           # Starts Grafana service
```

Test your installation by opening your VM's web browser then enter "http://localhost:3000". It should open a page that looks like this:

<img height="400" width="600" src="/tutorial_images/grafana.png"/>
