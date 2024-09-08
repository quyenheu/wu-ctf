- Tiêu đề: baby WAFfles order
- Nội dung: XXE 

- Trước tiên mình vào view web và dùng thử tính năng. bắt lại api POST /apiorder
- Vào đọc source thì backend có xử lý 2 dạng dữ liệu là json (mặc định) và xml

![Alt text](<../image/25.1.png>)

- Tiếp đó mình code lại để thử payload với hàm simplexml_load_string

![Alt text](<../image/25.2.png>)

- Cầm payload và lên đọc thử /etc/passwd

![Alt text](<../image/25.3.png>)

- Và lấy flag thoi 

![Alt text](<../image/25.4.png>)

#hackerga2101: 