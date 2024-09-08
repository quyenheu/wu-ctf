- Tiêu đề: baby interdimensional internet
- Nội dung: RCE

- Là một bài baby cmdi trong python
- Mình đang cố tìm một bài blackbox thì ra ông này thật ra là white đội nốt black 

- Trước tiên view qua source html 

![Alt text](<../image/20.1.png>)

- Thấy hint hint :> /debug và truy cập vào bạn sẽ có file sourc, lừa quá

![Alt text](<../image/20.2.png>)

- Vì source bé nên cũng không khó nhận ra họ đang thực hiên exec với input đầu vào 

![Alt text](<../image/20.3.png>)

- Tuy nhiên với GET request thì hoàn toàn random nên không thể kiểm soát được
- Còn POST request thì chúng ta sẽ kiểm soát hoàn toàn cả 2 tham số ingredient và measurement

![Alt text](<../image/20.4.png>)

- Mình gửi thử req để thao túng đầu ra và thành công thực hiện 68 + 86 
- Tiếp đến là inject code (đầu tiên mình dùng os nhưng fail vì không biết khi thực thi xong sẽ exit và kết quả không được trả về)

![Alt text](<../image/20.5.png>)

- Và lụm cờ 

![Alt text](<../image/20.6.png>)

#hackerga2101: