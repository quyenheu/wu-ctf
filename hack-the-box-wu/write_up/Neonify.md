- Tiêu đề: Neonify
- Nội dung: SSTI ERB ruby

- Có vẻ bài này mình từng làm rồi nên cũng không lâu để có flag 
- Nhưng lần trước là blackbox giờ là whitebox cũng là trải nghiệm khác

![Alt text](<../image/4.1.png>)
- web cho bạn nhập vào 1 kí tự nếu trong whitelist thì sẽ được in ra 
- Feature này tương ứng với với request post với body là neon 
![Alt text](<../image/4.2.png>)

- Đọc qua code để hiểu chức năng của hàm này 
![Alt text](<../image/4.3.png>)

- Họ cho bạn nhập từ 0-9a-z nếu có kí tự khác sẽ in dòng chữ 'malacious'
- Có vẻ coder hơi tự tin quá vào whitelist mà để thẳng untrusted data neon vào hàm in (lỗi SSTI, XSS, HTMLi, ...)
- vậy sẽ ra sao nếu ta ngắt dòng để whitelist không tới dòng tiếp theo

![Alt text](<../image/4.4.png>)
- Thành công ngắt dòng và đọc /etc/passwd
![Alt text](<../image/4.5.png>)
- Và Lụm cờ
#hackerga2101:
- Không biết ông nào đạo ông nào chứ challenge giống từ frontend đến cách khai thác :>