- Tiêu đề: C.O.P
- Nội dung: SQLi to deserialize in python

- Web bán các sản phẩm dưa chuột
- Quên không cap màn hình mấy ảnh web :<

- Vì chỉ có tính năng view sản phẩm nên mình cũng đọc source luôn 

![Alt text](<../image/5.1.png>)
![Alt text](<../image/5.2.png>)
- Thấy luôn SQLi nè, SQLmap thử cho vui chứ source có file schema.sql
- Tiếp đến là những đoạn sử dụng hàm pickle (tương đương với unserialize trong PHP)

![Alt text](<../image/5.3.png>)

- Đoạn này dump items để lưu vào database 

![Alt text](<../image/5.4.png>)
- Loads lại data đó và đoạn code gọi hàm loads là: 
![Alt text](<../image/5.5.png>)

- Serialize trong PHP phải dựa vào sự tiềm ẩn của các magic method nên impact sẽ khác nhau. Nhưng trong Python pickle không như vậy

![Alt text](<../image/5.6.png>)

- Giờ ren thử 1 payload và chứng minh nó có loads lại data do mình inject

![Alt text](<../image/5.7.png>)

- POC tạo POC :v 

![Alt text](<../image/5.8.png>)

- Và lụm cờ th 

![Alt text](<../image/5.9.png>)

#hackerga2101: