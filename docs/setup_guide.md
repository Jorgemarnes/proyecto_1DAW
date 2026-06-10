# Setup Guide

This guide explains how to configure the virtual machine infrastructure for the **Music Store - Static Site Generator Project** from scratch.

The project uses two Linux Mint virtual machines:

| Virtual Machine | Role            |        IP Address |
| --------------- | --------------- | ----------------: |
| VM-WEB          | Web server      | `10.109.15.17/24` |
| VM-BBDD         | Database server | `10.109.15.16/24` |

The web server runs **Nginx** and serves the generated static website.
The database server runs **PostgreSQL** and stores the music product data.

---

## 1. Infrastructure Overview

The project follows this architecture:

```text
Host Machine / Browser
        |
        | HTTP - Port 80
        v
VM-WEB - 10.109.15.17
        |
        | PostgreSQL - Port 5432
        v
VM-BBDD - 10.109.15.16
```

The host machine is used to open the website in a browser.
The VM-WEB machine serves the static HTML files.
The VM-BBDD machine stores the PostgreSQL database.

---

## 2. VirtualBox Network Configuration

Before configuring Linux Mint, both virtual machines must have the correct network adapters.

### VM-WEB

Recommended configuration:

| Adapter   | Mode                         | Purpose                            |
| --------- | ---------------------------- | ---------------------------------- |
| Adapter 1 | NAT                          | Internet access                    |
| Adapter 2 | Host-Only / Internal Network | Private communication with VM-BBDD |

### VM-BBDD

Recommended configuration:

| Adapter   | Mode                         | Purpose                                         |
| --------- | ---------------------------- | ----------------------------------------------- |
| Adapter 1 | NAT                          | Internet access, needed for installing packages |
| Adapter 2 | Host-Only / Internal Network | Private communication with VM-WEB               |

Both machines must be connected to the same private network.

---

## 3. Check Network Interface Names

Start both virtual machines and run the following command on each one:

```bash
ip a
```

or:

```bash
nmcli device status
```

In our case, the interfaces are:

| Interface | Machine | Purpose                |
| --------- | ------- | ---------------------- |
| `enp0s3`  | VM-WEB  | DHCP / NAT             |
| `enp0s8`  | VM-WEB  | Static private network |
| `enp0s8`  | VM-BBDD | Static private network |

If the interface names are different, replace them in the configuration files.

---

## 4. Configure Static IP on VM-WEB

On the web server virtual machine, edit the Netplan configuration file:

```bash
sudo nano /etc/netplan/1-network-manager-all.yaml
```

Add the following configuration:

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s3:
      dhcp4: true
    enp0s8:
      dhcp4: no
      addresses:
        - 10.109.15.17/24
```

Save the file and apply the configuration:

```bash
sudo netplan apply
```

Check that the IP address was assigned correctly:

```bash
ip a
```

The VM-WEB machine should show:

```text
10.109.15.17/24
```

---

## 5. Configure Static IP on VM-BBDD

On the database virtual machine, edit the Netplan configuration file:

```bash
sudo nano /etc/netplan/1-network-manager-all.yaml
```

Add the following configuration:

```yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    enp0s8:
      dhcp4: no
      addresses:
        - 10.109.15.16/24
```

Save the file and apply the configuration:

```bash
sudo netplan apply
```

Check that the IP address was assigned correctly:

```bash
ip a
```

The VM-BBDD machine should show:

```text
10.109.15.16/24
```

---

## 6. Test Network Communication Between VMs

From VM-WEB, test the connection to VM-BBDD:

```bash
ping 10.109.15.16
```

From VM-BBDD, test the connection to VM-WEB:

```bash
ping 10.109.15.17
```

If both commands return responses, the private network between both virtual machines is working correctly.

Example of a successful response:

```text
64 bytes from 10.109.15.16
```

To stop the ping command, press:

```text
CTRL + C
```

---

## 7. Install PostgreSQL on VM-BBDD

On the database virtual machine, update the package list:

```bash
sudo apt update
```

Install PostgreSQL:

```bash
sudo apt install postgresql postgresql-client -y
```

Check the PostgreSQL service status:

```bash
sudo systemctl status postgresql
```

Enable PostgreSQL to start automatically:

```bash
sudo systemctl enable postgresql
```

---

## 8. Set a Password for the PostgreSQL User

Enter PostgreSQL as the default `postgres` user:

```bash
sudo -u postgres psql
```

Set a password:

```sql
ALTER USER postgres WITH PASSWORD 'postgres';
```

Exit PostgreSQL:

```sql
\q
```

For a class project, the password `postgres` is enough for testing, but in a real environment a stronger password should be used.

---

## 9. Create the Project Database

Enter PostgreSQL again:

```bash
sudo -u postgres psql
```

Create the project database:

```sql
CREATE DATABASE music_store;
```

Check that the database exists:

```sql
\l
```

Exit PostgreSQL:

```sql
\q
```

---

## 10. Configure PostgreSQL to Accept Connections From VM-WEB

By default, PostgreSQL only accepts local connections.
We need to allow VM-WEB to connect to VM-BBDD through port `5432`.

Edit the PostgreSQL configuration file:

```bash
sudo nano /etc/postgresql/*/main/postgresql.conf
```

Find this line:

```conf
#listen_addresses = 'localhost'
```

Replace it with:

```conf
listen_addresses = '10.109.15.16'
```

Now edit the client authentication file:

```bash
sudo nano /etc/postgresql/*/main/pg_hba.conf
```

Add this line at the end of the file:

```conf
host    all    all    10.109.15.17/32    scram-sha-256
```

This allows only the VM-WEB machine to connect to PostgreSQL.

Restart PostgreSQL:

```bash
sudo systemctl restart postgresql
```

Check that PostgreSQL is listening on port `5432`:

```bash
sudo ss -tulpn | grep 5432
```

The output should show PostgreSQL listening on:

```text
10.109.15.16:5432
```

---

## 11. Configure the Firewall on VM-BBDD

If UFW is enabled, allow PostgreSQL connections only from VM-WEB:

```bash
sudo ufw allow from 10.109.15.17 to any port 5432 proto tcp
```

Enable UFW:

```bash
sudo ufw enable
```

Check the firewall status:

```bash
sudo ufw status
```

---

## 12. Install pgAdmin4 on VM-BBDD

The project requires pgAdmin4 as a PostgreSQL administration tool.

The database virtual machine uses **Linux Mint 21.2 Victoria**, which is based on **Ubuntu 22.04 Jammy**.
Because of this, the `jammy` repository must be used instead of the Linux Mint codename `victoria`.

Install required packages:

```bash
sudo apt update
sudo apt install curl ca-certificates gnupg -y
```

Add the pgAdmin4 official key:

```bash
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg
```

Add the pgAdmin4 repository for Ubuntu Jammy:

```bash
sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/jammy pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list'
```

Update the package list:

```bash
sudo apt update
```

Install pgAdmin4 Desktop:

```bash
sudo apt install pgadmin4-desktop -y
```

Open pgAdmin4 from the Linux Mint application menu.

---

## 13. Connect pgAdmin4 to PostgreSQL

Open pgAdmin4 and create a new server connection:

```text
Servers → Register → Server
```

In the **General** tab:

```text
Name: PostgreSQL VM-BBDD
```

In the **Connection** tab:

```text
Host name/address: localhost
Port: 5432
Maintenance database: postgres
Username: postgres
Password: postgres
```

Since pgAdmin4 is installed on the same virtual machine as PostgreSQL, the host is:

```text
localhost
```

---

## 14. Install Nginx on VM-WEB

On the web server virtual machine, install Nginx:

```bash
sudo apt update
sudo apt install nginx -y
```

Start Nginx:

```bash
sudo systemctl start nginx
```

Enable Nginx to start automatically:

```bash
sudo systemctl enable nginx
```

Check the service status:

```bash
sudo systemctl status nginx
```

---

## 15. Configure Nginx

Edit the default Nginx configuration file:

```bash
sudo nano /etc/nginx/sites-available/default
```

Use the following configuration:

```nginx
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /home/serverproject1daw/proyecto_1DAW/src/ssg;

    index index.html;

    server_name musicstore.com www.musicstore.com;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

This configuration tells Nginx to serve the static files located in:

```text
/home/serverproject1daw/proyecto_1DAW/src/ssg
```

The main page must be called:

```text
index.html
```

Test the Nginx configuration:

```bash
sudo nginx -t
```

If the configuration is correct, reload Nginx:

```bash
sudo systemctl reload nginx
```

---

## 16. Create a Test HTML Page

If the static site has not been generated yet, create a temporary `index.html` file:

```bash
nano /home/serverproject1daw/proyecto_1DAW/src/ssg/index.html
```

Add this content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Music Store</title>
</head>
<body>
    <h1>Music Store is working</h1>
    <p>Nginx is serving the static website correctly.</p>
</body>
</html>
```

Save the file.

---

## 17. Test the Web Server

From VM-WEB, test Nginx locally:

```bash
curl http://localhost
```

From the host machine, open a browser and visit:

```text
http://10.109.15.17
```

If the page loads, the web server is working correctly.

---

## 18. Configure Local Domain Name

The Nginx configuration uses the following domain names:

```text
musicstore.com
www.musicstore.com
```

To make them work locally, add this line to the host machine `hosts` file:

```text
10.109.15.17 musicstore.com www.musicstore.com
```

After that, the website can be accessed from the host browser using:

```text
http://musicstore.com
```

or:

```text
http://www.musicstore.com
```

---

## 19. Final Validation Checklist

The configuration is correct if all these tests work:

### VM-WEB IP

```bash
ip a
```

Expected IP:

```text
10.109.15.17/24
```

### VM-BBDD IP

```bash
ip a
```

Expected IP:

```text
10.109.15.16/24
```

### Ping from VM-WEB to VM-BBDD

```bash
ping 10.109.15.16
```

### Ping from VM-BBDD to VM-WEB

```bash
ping 10.109.15.17
```

### PostgreSQL status on VM-BBDD

```bash
sudo systemctl status postgresql
```

### Nginx status on VM-WEB

```bash
sudo systemctl status nginx
```

### Website access from host

```text
http://10.109.15.17
```

or:

```text
http://musicstore.com
```

---

## 20. Conclusion

After completing this setup, the project infrastructure is ready.

The VM-WEB machine serves the Music Store static website using Nginx.
The VM-BBDD machine stores the PostgreSQL database and can be managed using pgAdmin4.
Both virtual machines communicate through a private network using static IP addresses.

This setup satisfies the project requirement of separating the web server and the database server into two different virtual machines.
