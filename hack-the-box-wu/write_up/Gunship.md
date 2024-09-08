- Tiêu đề: Gunship
- Nội dung: proto inject to RCE, CVE-2020-36632

- Nghiêm túc chưa hiểu sao bài này very easy
- Vừa nạp card 1 tiếng bay vào làm hãi thật sự

- Bài này mình research nhiều và payload cũng không phải mình nghĩ (chưa đủ trình :v)

![Alt text](<../image/8.1.png>)

- Web khá đơn giản cho bạn nhập tên và nếu đúng với danh sách thì sẽ in ra màn hình 

![Alt text](<../image/8.2.png>)

- File source không có vuln gì cả vậy mình đoán là do thư viện nên đã đi research 
- Search thằng Flat đúng là có vuln, cụ thể dưới 5.0.1
![Alt text](<../image/8.4.png>)

- Check thì web đang dùng 5.0.0 vừa khéo 

![Alt text](<../image/8.3.png>)

- Do CVE này rất ít người giải thích nên có hai nguồn bạn có thể xem 
+ https://security.snyk.io/vuln/SNYK-JS-ARRFLATTENUNFLATTEN-598396
-> Không chi tiết nên mình không đủ trình follow
+ https://http418infosec.com/tag/unflatten
-> Dường như là 1 bài giống hệt (Nhưng mình khai thác khác nha)

- Đọc sơ qua để hiểu và ứng dụng payload inject cat thử /etc/passwd

![Alt text](<../image/8.5.png>)

- Mình không có quyền :> 

- AE để ý khi inject proto thì muốn xem kết quả sẽ phải 

![Alt text](<../image/8.9.png>)

- Nếu không lỗi là đúng 
- Nếu lỗi thì sẽ biết là lỗi gì luôn 

- Sau rất nhiều lần thử cat flag và check thư mục hiện tại mình biết: 
![Alt text](<../image/8.7.png>)
- Đây là thư mục chứa flag, nhưng flag có kí tự random không như source 
![Alt text](<../image/8.8.png>)

- Một điểm hạn chế nữa là server chặn rất nhiều 

![Alt text](<../image/8.6.png>)

- Ngoài ra curl, ping, python, ... đều bị chặn 
- Nhưng lại lọt khá buồn cười: sh, nc, head 

- Giờ hoàn toàn tạo được reverse shell từ sh và nc (Hướng 1)

![Alt text](<../image/8.10.png>)

- Nhưng không hiểu sao rất lag và chậm mình không connect được 
- Nên phải làm cách 2 là Blind đọc file flag 
- Với một đoạn code py đơn giản với ý tưởng: 
+ Cắt từng kí tự của file fl* so sánh nếu đúng in 1 (sẽ có kết quả trả về), nếu sai curl đến a.com (sẽ báo lỗi vì server không có curl)

![Alt text](<../image/8.11.png>)

- Thật ra blind cũng lag nên thi thoảng phải vào check lại

HTB{wh3n_lif3_g1v3s_y0u_p6_st4rT_p0llut1ng_w1th_styl3!!}

- Nhớ là không để *&. không là mệt luôn ấy 

#hackerga2101:
- Thực sự là 1 bài khó vì không có chi tiết về CVE và bản chất lỗi đã khó rồi 
- Stress 12h làm bài vreasy ngủ ngon mai đi học nhưng không giờ là 3:30