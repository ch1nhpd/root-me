- Có filter lọc ko cho nhập chứ cái. Nhưng mình còn có thể dùng kí tự `_ `để đặt tên biến. 
```php
$_=[];
$_=@"$_"; 
$_=$_['!'=='@']; //A
$___=$_; // chạy đến đây thì được kí tự $___=$_=A
```
- Trong php còn có kiểu ++$_ để tăng kí tự lên
VD: lúc đầu $_ = 'A' thì sau khi ++$_ thì $_ = 'B'
- Tuy nhiên nó chỉ áp dụng cho các chứ cái thôi(AZaz). Còn nếu $_ ='z'thì sau khi ++$_ thì $_ ='aa'



