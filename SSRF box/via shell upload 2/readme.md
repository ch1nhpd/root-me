# upload shell + overide /etc/passwd

## Step 1: scan -> port 6379 (redis)
## Step 2: create PHPshell by gopherus
> gopherus --exploit redis

(cũng có thể dùng [shell upload script](creSSH1.py))
## Step 3: overide /etc/passwd to insert user tor with root privilege. (Run attack.py)
## Step 4: 
> ssh  tor@ctf01.root-me.org 

### Happy hacking!!