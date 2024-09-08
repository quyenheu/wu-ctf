- Tiêu đề: LoveTok
- Nội dung: PHP code injection

- Web dự đoán tình yêu đến cho dân FA

![Alt text](<../image/2.1.png>)

- Khi bạn dùng tính năng try again! sẽ có 1 request như sau 

![Alt text](<../image/2.4.png>)

- Vì là whitebox nên rất dễ detech lỗi, cụ thể như sau:

![Alt text](<../image/2.3.png>)
- Class TimeController nhận vào untrusted data format và truyền vào hàm getTime() của class timeModel
- Mà hàm getTime lại lấy chính format đó bỏ thẳng vào hàm eval()
-> Inject thực thi được code PHP 

![Alt text](<../image/2.5.png>)

- Nhưng source có dùng hàm addslash() vậy nên payload thông thường sẽ bị 500
- Lách nhẹ với $_GET :v 

![Alt text](<../image/2.6.png>)
- Và lụm cờ 
![Alt text](<../image/2.7.png>)

#hackerga2101:
- Seo cùng là mức độ easy mà độ khó lại khác nhau z nhỉ :v 