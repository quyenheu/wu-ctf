- Tiêu đề: CurlAsAService
- Nội dung: cmdi

- Mình đọc source và thấy họ filter cmdi bằng hàm escapeshellcmd (hàm này bypass được)

![Alt text](<../image/38.1.png>)

- Mình từng gặp kiểu filter này rồi (cụ thể là bạn không thể escape để thêm lệnh nhưng có thể lợi dụng các option khác của lệnh đang sử dụng) 

![Alt text](<../image/38.2.png>)

- Và Inject -F pass=@/flag

![Alt text](<../image/38.3.png>)

![Alt text](<../image/38.4.png>)

#hackerga2101: