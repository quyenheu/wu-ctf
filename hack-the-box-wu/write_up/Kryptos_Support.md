- Tiêu đề: Kryptos Support
- Nội dung: XSS to IDOR 

- Với giao diện đầu tiên mình test qua thì nhận được XSS ở ô nhập 

![Alt text](<../image/33.1.png>)
![Alt text](<../image/33.2.png>)

- Tiếp đó thì gửi thử xem có cookie nào không 

![Alt text](<../image/33.3.png>)

- Mình thêm cookie và access vào /tickets 

![Alt text](<../image/33.4.png>)

- Nhưng đây không phải tài khoản của admin. Mình thử crack jwt nhưng không thành công 
- Thử qua chức năng settings, mình đổi được mật khẩu của tài khoản hiện tại 

![Alt text](<../image/33.5.png>)

- Mình thử đổi uid và thành công đổi mật khẩu admin

![Alt text](<../image/33.6.png>)

- Và login vào lấy được flag của chall 

![Alt text](<../image/33.7.png>)

#hackerga2101: