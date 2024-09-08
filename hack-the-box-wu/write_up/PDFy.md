Tiêu đề: PDFy
Nội dung: wkhtmltopdf SSRF

- wkhtmltopdf là thư viện trong linux dùng để chuyển html thành pdf 
- Thư viện này dính 1 lỗ hổng SSRF dẫn tới việc đọc file server. Và chall này ta cần đọc /etc/passwd

![Alt text](<../image/48.1.png>)

- Khi nhập một url bị lỗi hay không phải url thì sẽ nhìn rõ được câu lệnh 
- Ban đầu mình thử bypass để cmdi nhưng không thành công. Và follow post phía dưới để làm

![Alt text](<../image/48.2.png>)

- Host 1 php server với nội dung header trỏ về file:///etc/passwd
- Tiếp đó thì tạo 1 trang html với iframe kéo nội dung trang php trên về 

![Alt text](<../image/48.3.png>)

- Public với ngrok (nên để tcp vì http sẽ bị quần què)

![Alt text](<../image/48.4.png>)

- Kéo link về và lấy cờ

![Alt text](<../image/48.5.png>)

#hackerga2101:
https://exploit-notes.hdks.org/exploit/web/security-risk/wkhtmltopdf-ssrf/