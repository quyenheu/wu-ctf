- Tiêu đề: ApacheBlaze
- Nội dung: Request Smuggling, CVE-2023-25690

- Đây là 1 thử thách khá khó vì mình không giỏi vụ apache và smuggling
- Nhưng cũng may là có POC để follow 
- Bài code rất đơn giản 

![Alt text](<../image/7.1.png>)

- Chúng ta chỉ cần follow vào vòng elif này vì cơ bản là không có lỗi trong code khác
- Mình cũng đơn giản nghĩ là thêm header 'X-Forwarded-Host' nhưng cũng biết không được vì đây là htb

![Alt text](<../image/7.2.png>)

- Tiếp đến mình đọc file httpd.conf cũng chưa hiểu được nhiều và nhờ chatGPT hướng dẫn 
- Mình build lại trên local và sửa vòng elif trên thành in ra giá trị nếu có tồn tại của header 'X-Forwarded-Host'
- Khá bất ngờ vì giá trị lại bằng 'localhost:8001' sau một hồi research mình tìm được đoạn giải thích 'Nếu không code để flask tin tưởng header
nó sẽ bỏ qua và lấy giá trị của host' - maybe đúng sai nha

- Okay giờ khó để tìm lỗi trong code quay trở lại câu chuyện apache, lại là công cuộc research vuln thôi. rõ ràng chỉ có phần rewriterule và mycluster là liên quan đến xử lý request chính 
- Đi research và có kết quả sau 
![Alt text](<../image/7.3.png>)

- Một CVE về smuggling rất mới 2023 (đầu là mình bỏ qua vì không nghĩ lab mới đến thế :v)
- Xong sau đọc lại POC và exploit thử và thành công smuggling (Link bên dưới)

![Alt text](<../image/7.5.png>)
- Mình làm trên local và có debug code nên dễ dàng biết giá trị của 'X-Forwarded-Host' hiện tại 
![Alt text](<../image/7.7.png>)
- Phải bỏ bớt header để chuẩn ảo thật chứ :>
![Alt text](<../image/7.8.png>)

- Cầm payload lên và lụm cờ 

#hackerga2101:
- Link research: https://github.com/dhmosfunk/CVE-2023-25690-POC
- Mình đi sai 2 hướng sau: 
- Cái 1 là vì dùng param miner được header max-forwards (định nghĩa hơi oằn) kiểu mình nghĩ dùng để đi qua và lặp lại request :v 
![Alt text](<../image/7.4.png>)
- Cái 2 là quả XXS để lên ý tưởng XSS xong nhờ nó gửi hộ request mà cùng fail 
![Alt text](<../image/7.6.png>)
- Writeup nhưng hơi dài sr :v 