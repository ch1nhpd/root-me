# ...??...
## Step 1: Run creSSH1.py
## Step 2: create ssh key
> ssh-keygen -t rsa -C "root@ctf01.root-me.org"
## Step 3: Run creSSh2.py 
up public key to server
## Step 4: connect SSH by private key
> ssh -i .ssh/id_rsa root@ctf01.root-me.org