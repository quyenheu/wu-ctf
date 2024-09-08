- tiêu đề: magic login harder (bản nâng cấp của magic login mà nâng cấp vl)
- nội dung: RCE 

- vì là whitebox nên cứ lao vào đọc source thoi 

![Alt text](<../image/54.1.png>)

- không như magic login ở đây không có loose compase (và php cũng là bản 8. nên càng không có)
- nhưng mình từng gặp 2 string có cùng md5 rồi nên cũng không lạ nữa 

![Alt text](<../image/54.2.png>)

- với 2 mã trên thì khi md5 sẽ cho cùng kết quả và việc còn lại là thêm base64 

![Alt text](<../image/54.3.png>)

- mình cầm kết quả đi login thử lại nhận được lỗi header... khá hoang mang nên quay vào đọc lại code 

![Alt text](<../image/54.4.png>)

- nếu chú ý kĩ thì họ code header() nhưng không exit hệ quả gây ra lỗi 
- nhưng hàm session đã được set nên hoàn toàn có thể truy cập vào /admin.php

![Alt text](<../image/54.6.png>)

- đọc qua code trang /admin.php thì thấy có lỗi liền, mình path traversal thử 

![Alt text](<../image/54.5.png>)

- nhưng file flag lại là random với 5 kí tự nữa thì chắc chắn phải rce mới lấy được. giờ mình nghĩ ra 4 hướng như sau 

- Hướng 1: include 1 trang code php từ ngoài internet (không thành công vì có lẽ họ config allow_url_include = Off)
![Alt text](<../image/54.7.png>)
- Hướng 2: inject shell vào file log và mail (không thành công vì log được đẩy lên docker chứ không lưu lại trên server)
![Alt text](<../image/54.11.png>)
- Hướng 3: một hướng mình reseach và thật sự chưa hiểu lắm :v 
https://book.hacktricks.xyz/pentesting-web/file-inclusion/lfi2rce-via-nginx-temp-files
- Hướng 4: inject shell vào session và tìm file lưu (thành công bởi vì nếu bạn nối thêm 1 đoạn kí tự giống nhau thì khi hash vẫn giống nhau)
![Alt text](<../image/54.9.png>)
![Alt text](<../image/54.10.png>)

#hackerga2101:
- Lại underrate siêu điển hình của cookie 
- làm oải cả người mới được :v