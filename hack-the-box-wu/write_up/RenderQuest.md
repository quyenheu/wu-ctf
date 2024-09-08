- Tiêu đề: RenderQuest
- Nội dung: SSTI to RCE 

- Thú thật thì mở source Golang ra cũng hơi hãi vì mình không giỏi nó 
- Phải tra kha khá mới hiểu được source :v dù nó bé tí 

- Lướt web dùng thử đây là trang cho bạn render lại link url nhập vào (+untrusted data)
![Alt text](<../image/6.4.png>)

- Vào sâu web thì thấy có hàm exec command khá vip 
![Alt text](<../image/6.1.png>)

- Nhưng tiếc là đầu vào lại toàn cố định 

![Alt text](<../image/6.2.png>)

- Thử render web do mình kiểm soát chúng ta có vài lỗi (XSS, HTMLi, SSTI, ...)

![Alt text](<../image/6.3.png>)

- Đương nhiên target là SSTI vì flag nằm ở root
- Sau khi research mình khá bất ngờ vì SSTI ở Golang đặc biệt có thể tự gọi hàm và truyền tham số 
- Link bài sẽ để dưới
![Alt text](<../image/6.5.png>)
![Alt text](<../image/6.6.png>)

- Mà mình đã có hàm thực thi exec từ trước, giờ đơn giản sửa payload phía web mình kiểm soát là được 
![Alt text](<../image/6.7.png>)
![Alt text](<../image/6.8.png>)
- Và lụm cờ 
![Alt text](<../image/6.9.png>)

#hackerga2101:
- Link research: https://www.onsecurity.io/blog/go-ssti-method-research/
- Newbie Golang Hắc cơ Gà :v