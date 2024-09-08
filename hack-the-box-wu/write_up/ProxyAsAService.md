- Tiêu đề: ProxyAsAService
- Nội dung: SSRF to read environ file

- Một bài hay về việc ssrf và một số tip trick

![Alt text](<../image/18.9.png>)

- Khi truy cập vào bạn sẽ nhận được 1 giao diện từ reddit.com theo url(Nhưng không phải redirect mà là dạng kéo source về)

- Lao vào đọc source để hiểu hơn về web
- Có dòng requests.get là mình sửa để exploit trên local nhé :v 
![Alt text](<../image/18.1.png>)
![Alt text](<../image/18.8.png>)
- Thì target_url bị cố định là 'reddit.com' + url do mình truyền vào 

- Tiếp tục đọc source để xác định mục tiêu. Thì mình thấy flag nằm trong dockerfile
- Và có debug.route /environment có in ra biến os.environ

![Alt text](<../image/18.3.png>)
![Alt text](<../image/18.4.png>)

- Mình sửa lại code và chứng mình có flag khi ta access được vào /debug/environment
- Okay như đã biết ở trên thì backend có hàm truy cập đến target_url vậy có cách nào để nhờ nó truy cập hộ đến /debug/environment hộ mình không (vì /debug/environment có hàm check ip từ local) mặc dù target_url đã bị fix cứng 1 phần 

- Đương nhiên là có :> (Mình có nghĩ 1 hướng khá oke mà không exploit được sẽ trình bày ở cuối)
- Url ngoài domain bạn có thể truyền username:password lên nữa 
- Theo GPT 'sitename.com@hackerga.com có thể được xem xét như là một dạng đặc biệt của URL chứa thông tin xác thực (authentication information) tương tự như username:password. Mặc dù không phải mọi server hoặc ứng dụng web đều xử lý đúng cách, một số server có thể xử lý URL này và chấp nhận nó làm phương tiện để xác thực.' 

- Và thực sự hàm request nó  dịch thằng http://a.com@hacker.com thành http://hacker.com
- Một tip khá mới cho mình 

- Giờ đã biết cách thao túng thì chúng ta cần làm gì tiếp theo 
- Phải bypass qua 2 hàm check là is_from_localhost và is_safe_url 

- Mình cần truyền vào url=@0.0.0.0:1337/debug/environment (1337 vì trên local host từ 1337 ra port bạn đang chạy)

- Ngoài 0.0.0.0 bạn có thể thử ::1 hoặc dạng hex đều là localhost

![Alt text](<../image/18.5.png>)

#hackerga2101:
- Ý tưởng khác của mình là biến reddit.com fix cứng kia thành subdomain của domain mình kiểm soát 
![Alt text](<../image/18.2.png>)

- Bạn có thể nạp card ngrok để kiểm soát response trả về theo ý mình 
- Giờ hãy sửa response thành script fetch('http://0.0.0.0:1337/debug/environment') để nó tự động fetch đến và console.log ra 
- Nhưng có vẻ mình đã bị chặn vì policy

![Alt text](<../image/18.7.png>)

- Note: Giờ có thêm tip http://user:pass để test r kk