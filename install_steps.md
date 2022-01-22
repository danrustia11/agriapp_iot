# Setting up your RPi

1. Install Apache: <br/>

   ```bash
   sudo apt-get update <br/>
   sudo apt-get install apache2 -y <br/>
   sudo usermod -a -G www-data pi <br/>
   sudo chown -R -f www-data:www-data /var/www/html <br/>
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
