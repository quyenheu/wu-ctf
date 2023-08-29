- tiêu đề : web4

- FUN FACT : okay cuối cùng thì cũng có 1 bài thú vị hehe, và vì là wu nên mình không giải thích các hướng mình đi nha :> 

- trước tiên vào view page đã thấy ối dồi ôi rồi (mu ng* suuuuuu)
![Alt text](<./img/4.1.png>) 

- okay thì mình view cookie bắt được thằng session khá thú vị trông có %3D nên mình đi url decode 

![Alt text](<./img/4.2.png>)

- decode xong lại thấy giống base64 -> tiếp tục :> 

![Alt text](<./img/4.3.png>)

- ohla kiếm được 1 thằng json khá ngon heh thử đổi username thành 'admin' và isAdmin:true thì đúng là web nó welcome admin
- tiếp thử xem có được bỏ qua login không thì web nói éo :>
- mình đã xem wáppalizơ từ trước nên biết web code bằng js 
- ngờ ngợ vì trước mình từng làm 1 bài serialize nodejs và dữ liệu unserialize của nó thật sự khác các ngôn ngữ khác (kiểu như json giống trên kia) 

- hehe mình đi tìm luôn bài viết để đọc thêm :
https://opsecx.com/index.php/2017/02/08/exploiting-node-js-deserialization-bug-for-remote-code-execution/?fbclid=IwAR0_VTpLQDOvIcFVerYF9KpUX9TNsrdnfjbjGJ4r7fE3sXXoxYTZQd83KgE

- okay đúng thật là có lỗi nhé vì mình đọc nhiều hơn 1 bài viết kia và thử kha khá payload nó bắn lỗi tùm lum :> 
- mình bắt được một vài hạn chế của web này 
   + chúng ta không chạy được console.log nên không in được dữ liệu ra màn hình 
   + mình thử curl và con server không hiểu curl luôn :> 
   + vậy chắc là server mới toanh , nên thử ghi lên document root (lúc bắn lỗi mình biết document root con này là /var/www/html) và đương nhiên không được :> 
-> chắc chỉ còn tạo reverse shell thoii 

- okay mình đọc bài hướng dẫn trên kia thì nó chỉ cách tạo rì vợt seo 
- ae tải file https://github.com/ajinabraham/Node.Js-Security-Course/blob/master/nodejsshell.py 
- chạy lệnh python2 nodejsshell.py yourip yourport 

![Alt text](<./img/4.4.png>)

- hehe vấn đề lại tiếp tục là ip của bạn là lan đâu có public sao con server nó kết nối được :> 
- giờ phải dùng ngrok ae ạ 
- chạy lệnh ./ngrok tcp yourport okay và giờ bạn nhận được 1 cái địa chỉ ip và port public thông về với ip local của bạn
- (đơn giản hiểu là con ngrok nó sẽ tạo 1 ip đứng ở giữa nhận kết nối ngược từ server rồi gửi về iplocal của bạn kiểu man in the middle á)

- chạy lệnh tạo shell với yourip (là cái ip của ngrok cho) yourport (là cái port của ngrok)
- encode base64 xong url đi 

- gửi lên server và nhận lại kết nối tới máy mình đọc file Dockerfile lụm cờ hoi 

#hackerga2101:
- wu của mình chia sẻ là chính và con server khá lag nên kết nối lại ngại lắm kkk ae đọc hiểu thui không có ảnh đoạn sau
- đánh giá thì bài này khá hay mình