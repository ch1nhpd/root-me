# Attacking JWT

## 1. Modify the algorithm to none

 https://token.dev/

## 2. Brute force key

https://github.com/aress31/jwtcat : fastest (ở bản gốc là dùng cho HS256, đã thử sửa thành HS512 -> done, sẽ thử với các cái khác sau...)

### 3. Change RS to HS

- khi chuyển từ RS -> HS thì server sẽ lấy cái public key của RS làm secret key cho HS. 
- Mà public key của RS thì mình đã biết nên.....

--- 
## Document

1. https://repository.root-me.org/RFC/EN%20-%20rfc7519.txt
2. https://jwt.io/introduction
3. https://repository.root-me.org/Exploitation%20-%20Web/EN%20-%20Hacking%20JSON%20Web%20Token%20(JWT)%20-%20Rudra%20Pratap.pdf
4. https://github.com/ticarpi/jwt_tool


Note: 
- Can use john to brure force secret key.
- https://jwt.io/ và  https://token.dev/ bổ trợ cho nhau. Dùng cái này ko đc thì chuyển cái kia. Nếu vẫn không đc thì dùng code: 
 ```python
import jwt

public = open('key.pem', 'r').read()
print (public)
print (jwt.encode({"username":"admin"}, key=public, algorithm='HS256')) 
print (jwt.encode({"username":"admin"}, key=public+'\n', algorithm='HS256')) # nếu file key ko có \n ở cuối

 ```