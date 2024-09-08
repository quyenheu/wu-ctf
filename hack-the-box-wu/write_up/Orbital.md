- Tiêu đề: Orbital
- Nội dung: Sqli to path traversal 

- Trước tiên thì họ để sqli ngay hàm login 

![Alt text](<../image/36.1.png>)

- Mình viết payload exploit nhưng do nó lưu dấu () và space để ghi pass trước khi hash nên không được 
- Đây là dạng subquery sqli time based
- Đóng tool vô 

![Alt text](<../image/36.2.png>)
- Tiếp đó ta thấy lỗi filter path traversal 

![Alt text](<../image/36.3.png>)

- Bypass bằng ..././ mình cat được /etc/passwd 
- Nhưng lại không tìm được file /flag.txt 
- Quay lại đọc dockerfile thì thấy nó được mount ra file khác 

![Alt text](<../image/36.5.png>)

- Cat flag thôi 

![Alt text](<../image/36.4.png>)

#hackerga2101: