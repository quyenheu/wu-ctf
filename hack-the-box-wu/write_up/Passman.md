- Tiêu đề: Passman
- Nội dung: Grapql injection

- Grapql là thứ gần như mình chưa đụng bao giờ nên cũng mò mẫm mãi
- Đầu tiên thì mình chú ý đến cái req resgister và code của nó 

![Alt text](<../image/35.4.png>)
![Alt text](<../image/35.5.png>)

- Nôm na là ở trong cái mutation nó require vài cái trường như username, email, password và truyền vào hàm ResgisterUser
- Ngay trong cái mutation đó có 1 hàm khác là updatePassword mình không thấy có feature này trên web

![Alt text](<../image/35.1.png>)

- Dù yêu cầu authen nhưng khi update hàm lại nhận tham số args.username thay vì request.user.username nên ta hoàn toàn injection để thay đổi password của admin được 

![Alt text](<../image/35.2.png>)

- Giờ thì login vào lấy cờ 

![Alt text](<../image/35.3.png>)

#hackerga2101: