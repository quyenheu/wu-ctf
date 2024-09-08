- Tiêu đề: Insomnia
- Nội dung: Logic code 

- Trang web có 2 tính năng chính là đăng ký đăng nhập 

![Alt text](<../image/47.1.png>)

- Với code xử lý index sẽ đưa bạn flag nếu bạn đăng nhập với username là administrator 

![Alt text](<../image/47.2.png>)

- Nhưng đương nhiên jwt secret không thể crack 
- Code hàm đăng nhập 

![Alt text](<../image/47.3.png>)

- Trong đây có một lỗi logic ở hàm so sánh !count($json) == 2
- Vì count($json) sẽ là số lương bạn biến trong json khi submit để login, nhưng nếu bạn chỉ truyền username -> count($json) sẽ là 1 
và !1 là false tiếp đó nó được so sánh yếu với 2 ( == ) mà false == 2 sẽ được kết là false nên ta bỏ qua được kiểm tra login 

![Alt text](<../image/47.5.png>)

- Thật ra với bất kỳ 1 số nguyên nào ngoài số 0 (vì !0 là true) ta đều có thể bỏ qua được kiểm tra login nhưng mình thử với số 3 
thì server trả 500 chắc là do cách xử lý chuỗi json của họ

![Alt text](<../image/47.4.png>)

#hackerga2101: