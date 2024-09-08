- Tiêu đề: Memo Baby CSRF
- Nội dung: CSRF giả mạo yêu cầu máy chủ 

- Là 1 bài whitebox nên mình có sửa source và build lại nên source có thể khác gốc

- Điều kiện có flag là ip request đến /flag/notice_flag=127.0.0.1 và userid=admin (userid thì dễ r)
![Alt text](<../image/56.6.png>)

- Mình sửa để khi có request đến /admin/notice_flag sẽ gửi ip và userid từ gói tin gửi tới lên server mình kiểm soát
- Bạn có thể để nó alert ra cũng được 

- ![Alt text](<../image/56.5.png>)

- Để ý route /flag khi xử lý POST request, sẽ gọi hàm check_csrf() 

![Alt text](<../image/56.1.png>)

- Hàm check_csrf(), kiểu urlencode, nhưng để ý biến url là request từ local 

![Alt text](<../image/56.2.png>)

- Sau đó lại gọi hàm read_url()

![Alt text](<../image/56.3.png>)

- Tóm tắt là sử dụng selenium để thực hiện thao tác và cuối cùng có dòng driver.get(url)
-> Url local nên server sẽ tự gửi và đương nhiên ip sẽ là 127.0.0.1

- Vậy giờ cần thao túng để cho url get vào route /admin/notice_flag 
- <img src='http://localhost:1337/admin/notice_flag?userid=admin'> payload để thỏa 2 điều kiện check trong /admin/notice_flag
- và flag sẽ được gắn vào biến memo_text 
- Giờ cần truy cập /memo để nhận giá trị flag trong biến memo_text (/memo in lại biến global memo_text)

#hackerga2101:
 
