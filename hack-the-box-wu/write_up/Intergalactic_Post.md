- Tiêu đề: Intergalactic Post
- Nội dung: SQLite inject to RCE 

- Mình từng làm SQLi upload file còn SQLite thì đây là lần đầu 
- Web có tính năng subcribe với email bạn nhập nhưng cũng không có dấu hiệu cụ thể chỉ được header đến /?...

![Alt text](<../image/29.8.png>)

- Sau khi view qua code mình phát hiện được lỗi SQLi

![Alt text](<../image/29.1.png>)

- Nếu có tồn tại header X-Forwarded-For hoặc ... thì biến $ip_address sẽ do mình kiểm soát 
- Biến $email đã bị filter 

![Alt text](<../image/29.2.png>)

- Nhưng ở câu lệnh query lại tryền thẳng dữ liệu nên ta hoàn toàn SQLi được 
- Mình chứng mình bằng time based 

![Alt text](<../image/29.3.png>)

- Nhưng vấn đề là flag được lưu ở / và có kí tự random thì SQLi đơn thuần không lấy được 
- Nên mình đi search và có tìm được lỗi để giải quyết bài (link dưới bài)

![Alt text](<../image/29.4.png>)

- Thực hiện inject và nối thêm câu lệnh tạo file lol.php với payload <?php system($_GET['cmd']);?>

![Alt text](<../image/29.5.png>)

- Truy cập và lấy cờ thôi 

![Alt text](<../image/29.6.png>)
![Alt text](<../image/29.7.png>)

#hackerga2101: 
- https://research.checkpoint.com/2019/select-code_execution-from-using-sqlite/
- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md