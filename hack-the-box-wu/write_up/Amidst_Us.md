- Tiêu đề: Amidst Us
- Nội dung: CVE-2022-22817 RCE in PIL lib

- Vì source nhỏ nên vừa vào mình cũng xác định luôn là có lỗi trong file util.py 
- Đi search một số hàm thì ImageMath.eval có thể thực thi code 

![Alt text](<../image/30.1.png>)

![Alt text](<../image/30.4.png>)

- Tiếp đó thì nhét payload vào (mình thử nhưng không curl hay reverse được)

![Alt text](<../image/30.2.png>)

- Và truy cập lấy cờ

![Alt text](<../image/30.3.png>)

#hackerga2101: