- Tiêu đề: Knife 
- Nội dung: cat 2 flag :v

- Sau khi connect mình nmap thử thì nhận thấy có 2 port 80 và 22 mở 
- Mình viết ip + tên lab vào file hosts và truy cập pentest thử 

![Alt text](<../image_machine/1.2.png>)

- Web không có feature và sau khi fuzzing, brute param, ... mình không nhận được gì 
- Đóng thử nuclei vào xem thêm thông tin thì nhận được ngay 1 critical 

![Alt text](<../image_machine/1.1.png>)

- Có thể tạo rev theo lỗi php v8.1.0
- Lên template search thử exploit  

![Alt text](<../image_machine/1.3.png>)

- Cụ thể là inject user-agent tạo rev như sau

![Alt text](<../image_machine/1.6.png>)

- Mình lưu file và chạy python3 exploit.py url_target ip_listen port_listen và thành công nhận rev 

![Alt text](<../image_machine/1.4.png>)

- Nhưng chỉ với quyền hạn user james 
- Tạm lấy được 1 cờ user 

![Alt text](<../image_machine/1.5.png>)

- Tiếp đó mình tải 1 file linpeas từ máy mình và exploit thử 
- Nhận thấy có lỗi của thằng knife 

![Alt text](<../image_machine/1.7.png>)

- Vì có thể sudo NOPASSWD nên mình search thử 

![Alt text](<../image_machine/1.8.png>)

- Exploit thử và thành công chạy lệnh dưới quyền root 
- Cat nốt flag còn lại

![Alt text](<../image_machine/1.9.png>)

#hackerga2101: