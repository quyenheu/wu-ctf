- Tiêu đề: Mutation Lab
- Nội dung: SVG inject to path traversal to authen :v

- Sau khi dùng thử 1 số tính năng của web mình chú ý vào chức năng chuyển svg sang png (khi bạn dùng export)

![Alt text](<../image/41.1.png>)
![Alt text](<../image/41.2.png>)

- Có thể thấy mình inject và tạo svg theo ý được 
- Đi research về lib kia 

![Alt text](<../image/41.3.png>)

- Cộng với follow bài exploit ở dưới

![Alt text](<../image/41.6.png>)
- Mình thành công path traversal đọc /etc/passwd

![Alt text](<../image/41.4.png>)

- Nhưng không có file /flag.txt hay /flag nên chắc chắn phải exploit thêm 
- Dùng lỗi trên đọc source của bài (khi bắn lỗi bạn thấy được /app là nơi lưu code)
- Trong file /app/routes/index.js có định nghĩa cách để có flag 

![Alt text](<../image/41.10.png>)

- Mình lấy được SESSION_SECRET_KEYS trong file /app/.env (bạn path traversal đọc file /app/index.js là thấy)

![Alt text](<../image/41.7.png>)
- Và trong file auth thì họ dùng secret này để tạo session 

- Mình code lại nodejs để tạo lại session với username = admin

![Alt text](<../image/41.8.png>)

- Quay lại /dashboard với session và session.sig mới 

![Alt text](<../image/41.9.png>)

- Thành công lấy được flag

#hackerga2101:
- Link exploit: https://github.com/neocotic/convert-svg/issues/81