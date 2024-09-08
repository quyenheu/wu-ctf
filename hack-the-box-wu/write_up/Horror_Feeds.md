- Tiêu đề: Horror Feeds
- Nội dung: SQLi

- Trước tiên đọc source và thấy có đoạn SQLi ở register

![Alt text](<../image/34.1.png>)

- Mình thử inject " và có bắn lỗi về hash của password = 1 

![Alt text](<../image/34.3.png>)

- Lợi dụng ON DUPLICATE KEY UPDATE để đổi lại password admin thành ý mình 

![Alt text](<../image/34.2.png>)

- Giờ login với account admin và password 1 

![Alt text](<../image/34.4.png>)

#hackerga2101: