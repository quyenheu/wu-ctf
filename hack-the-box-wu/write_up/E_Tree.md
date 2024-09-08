- Tiêu đề: E.Tree
- Nội dung: Xpath injection

- Đọc source thì mình thấy flag được lưu trong file xml 

![Alt text](<../image/39.1.png>)

- Doashboarh có thể hiển thị thông tin người dùng nhưng lại không thao túng được input 
- Chuyển hướng qua /search routes thì hàm search_staff đang bị xpathi

![Alt text](<../image/39.2.png>)

- Mình thử 1 payload và nhận lại được exits user
![Alt text](<../image/39.3.png>)

- Dùng substring cắt kí tự đầu ra để so sánh với chuẩn flag 

![Alt text](<../image/39.4.png>)

- Vì là blind nên mình code lại py để exploit 

![Alt text](<../image/39.5.png>)

- Nhưng chỉ exploit 1 nửa (đầu tiên mình nhìn file xml cũng biết là ở 2 user nhưng thử lại không được). có vẻ chall phần flag còn lại đã giấu ở trường nào đó khác selfDestructCode
- Nên mình dùng contains để check nếu trường nào có dạng flag thì lấy 
![Alt text](<../image/39.6.png>)

#hackerga2101: