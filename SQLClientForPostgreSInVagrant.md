### Problem ###

I have a Vagrant box (Ubuntu) setup with PostgreSQL on my Windows 7 host. I want to access the database using a SQL client (pgAdmin or HeidiSQL or DbVisualizer).  

### Solution ###

1.  `cd /etc/postgresql/9.3/main`
1.  Edit `pghba.conf` (the file can have a different name sometimes like this: `pg_hba.conf`).  
    1. On the last line, create a new row with the following 5 columns: `host all all all password`
    1. Save changes and exit.
1. Edit `postgresql.conf` (in the same directory).  
   1. `listen_addresses = '*'`
   1. Save changes and exit. 
1. Restart PostgresQL service in Ubuntu.
   1. `sudo service postgresql restart`
1. From within the SQL client, create a new connection. Put the IP of your Vagrant box and the port (usually `5432`). Also, put the username and password of your user.  

---

**Tip:** if you don't have a user, or dont' know what it is, you can always create a new superuser with a password with this command: `createuser -P -s -e <<usernamegoeshere>>`
