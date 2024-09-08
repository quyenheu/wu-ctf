- Tiêu đề: baby nginxatsu
- Nội dung: indexing to leak backup file 

- Trước tiên mình fuzzing qua thì có thấy file .htaccess và web.config có status 200 
![Alt text](<../image/26.1.png>)

- Sau khi đọc nội dung thì có thể thấy web bị indexing nên mình truy cập vào tất cả các thư mục tồn tại 

![Alt text](<../image/26.2.png>)

- Ở cuối /storage có để 1 file v1_db_backup_1604123342.tar.gz    
- Mình dowload về extract thì nhận được 1 file database.sqlite và load lại file này trong ubuntu

![Alt text](<../image/26.3.png>)

- Thành công lấy được email, password của admin
- Đi giải thử hash password lại xem được không 

![Alt text](<../image/26.4.png>)

- Thành công dịch ngược được và cầm email, password login lại thôi 

![Alt text](<../image/26.5.png>)

#hackerga2101: