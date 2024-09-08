- Tiêu đề: Spookifier
- Nội dung: SSTI to RCE


- Bài cho bạn nhập input và hiển thị input đó dưới 4 kiểu chữ (ô cuối cùng là bình thường có thể đọc)
- Whitebox nên sau khi đọc source mình thấy input được render thẳng 
- Python ${} nên là mako template

![Alt text](<../image/19.2.png>)
![Alt text](<../image/19.3.png>)

- Test thử ${7*7}

![Alt text](<../image/19.1.png>)

- Nhưng server chặn một số payload nên mình toàn bị 500

![Alt text](<../image/19.4.png>)
- Cóp nguyên đống payload trên payloadofallthings
- Mình tìm được một số cái bypass được 
![Alt text](<../image/19.5.png>)
- Lưu ý xíu là lúc mình làm quên để .read() nên không hiện kết quả :v
- Payload: ${self.module.cache.util.os.popen("cat /flag.txt").read()}

![Alt text](<../image/19.6.png>)

#hackerga2101: