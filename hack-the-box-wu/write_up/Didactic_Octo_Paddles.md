- Tiêu đề: Didactic Octo Paddles
- Nội dung: Jwt bypass to SSTI 

- Đọc source mình thấy có 2 lỗi khá dễ detech 

![Alt text](<../image/45.1.png>)

![Alt text](<../image/45.2.png>)

- Nếu mình authen được vào admin thì sẽ ssti được 

- Cài extens json web token và sử dụng chức năng để alg = NONE là bypass được authen 

![Alt text](<../image/45.3.png>)

- Vào thì ssti không filter 
![Alt text](<../image/45.4.png>)

![Alt text](<../image/45.5.png>)
#hackerga2101: