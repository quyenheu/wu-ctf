- Tiêu đề: BlinkerFluids
- Nội dung: md-to-pdf CVE-2021-23639

- Sau khi dùng thử và đọc source thì mình không phát hiện lỗ hổng 

![Alt text](<../image/28.1.png>)

- Nên đã đi search vuln về hàm md to pdf vì cũng nghi pdf inject 

![Alt text](<../image/28.5.png>)

- Kết quả là thu được CVE-2021-23639 md-to-pdf to RCE 
- Mình follow poc và đăng thử 1 file với nội dung curl ra webhook 

![Alt text](<../image/28.2.png>)

- Khi vào view file thì không thấy có kết quả gì 

![Alt text](<../image/28.3.png>)

- Nhưng thực chất là đã có req gửi lên webhook của mình (này là chứng minh vì lúc đầu mình dùng lệnh ls /)

![Alt text](<../image/28.4.png>)

- Giờ thì curl /flag.txt ra ngoài là được 

![Alt text](<../image/28.6.png>)

- Ngoài ra có thể làm được rev shell mà không cần thiết lắm 

![Alt text](<../image/28.7.png>)

#hackerga2101: 