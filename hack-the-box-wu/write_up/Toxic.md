- Tiêu đề: Toxic
- Nội dung: Serialize to RCE

- web không có tính năng nên mình vào đọc source luôn 

![Alt text](<../image/3.1.png>)

- Mở đúng 1 file nhìn __destruct() với include đoán luôn serialize :>>

![Alt text](<../image/3.2.png>)

- Và đúng thật là vậy. Vì source nhỏ nên cũng không khó detech 
- Mình custom lại file để serialize ra /etc/passwd

![Alt text](<../image/3.4.png>)
- Thay value của PHPSESSION và load lại trang 

![Alt text](<../image/3.3.png>)

- Nhưng vấn đề là file flag có 5 kí tự random nên phải đẩy impact của lỗi này lên RCE 
- Hàm include sẽ kéo mã PHP và thực thi nên phải inject code PHP sau đó include về 
- Thì dễ nhất là include access.log của server 
- Mình view access.log (/var/log/nginx/access.log) có thấy lưu user-agent(một trường mình kiểm soát được)

![Alt text](<../image/3.5.png>)

- Một pha chơi nguu phải load start lại lab :>>
![Alt text](<../image/3.7.png>)

- Làm lại inject <?php system('ls /')?>

![Alt text](<../image/3.8.png>)

- Và cat flag là có ngay 

![Alt text](<../image/3.10.png>)

#hackerga2101: