- Tiêu đề: PHP Inclusion via phpinfo
- Nội dung: LFI xàm

- Tên bài là một dạng khai thác khá hay của LFI 
- Nhưng sau một hồi race condition upload mình lại không nhận được shell code 
- Ngồi 2 tiếng sau với 1 payload phức tạp của dạng LFI filter mình để thực thi code được 

![Alt text](<../image/57.1.png>)
![Alt text](<../image/57.2.png>)

- Payload thực hiện sẽ chạy code php mà không cần lưu 

![Alt text](<../image/57.3.png>)

#hackerga2101:
- Hoặc là mình sai hướng làm =)))))
- https://book.hacktricks.xyz/pentesting-web/file-inclusion/lfi2rce-via-php-filters#full-script