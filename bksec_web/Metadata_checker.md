- tiêu đề : Metadata checker
- nội dung : RCE 

- uhm bài này mình thấy có 1 điểm mệt hơn xíu là đoạn unlink 1.5s 
- vì vào view source cái thấy luôn lỗi rồi mà :v 

- mình dùng thử tí thì web nó cho up jpg 
- okay mở source ra đọc 

![Alt text](<./img/2.2.png>)

- lỗi tùm lum :v 
- 1 là path traversal ở đoạn Cookie 
- 2 là kiểm tra lỏng vì check content-type 

- tìm được cơ sở rồi mình đám thoi :> 
- mình cũng up 1 thử 1 file ảnh và bắt lại sửa tham số 

![Alt text](<./img/2.1.png>)

- mình đoán document root là /var/www/html ( chứng minh đúng r nhá :> )
- nên path để nó tạo file tại document root với tên file php ( này ae sửa content-type là bypass được rồi )
- inject shell vào 

![Alt text](<./img/2.3.png>)

- nhưng khi truy cập vào me nó :> toàn not found 

- biết tính hay ẩu đả mình quay lại đọc code và y rằng 

![Alt text](<./img/2.4.png>)

- nó sẽ unlink sau 1.5s :>> khốn nạn thật 
- nhưng không sao vì vẫn > 0 xử lý được kkk 

- giờ có 2 hướng ae đủ nhanh tay là ăn :> 
- hoặc là code py 

- thật ra bài này nó để tận 1.5s dại gì ngồi code hehehe
- mình sẽ post bằng burp và get bằng py luôn hehe

![Alt text](<./img/2.5.png>)

- nhưng lỗi lại xảy ra vì trong 1 file ảnh có rất nhiều ký tự linh tinh nên đã vô tình làm hỏng nội dung file php 
- để ý họ chỉ lấy vài nội dung cơ bản mà nó chỉ ở đầu thôi -> mình xóa vài phần nội dung ảnh đi chừa lại chắc 50 dòng đầu 

![Alt text](<./img/2.6.png>)

![Alt text](<./img/2.7.png>)

#hackerga2101: 
- sẽ có ae thắc mắc là vì tên file tạo ra có thời gian nên sao biết mà get đúng không -> code py int(time.time()) + 1 dao động khoảng xíu này thoi hehe