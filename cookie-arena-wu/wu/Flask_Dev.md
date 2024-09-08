- Tiêu đề: Flask Dev
- Nội dung: Werkzeug / Flask Debug to RCE 

- Bài này mình làm 2 lần rồi nên cách khai thác nhớ vẫn rõ
- Flow: https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/werkzeug

- Đầu tiên là fuzzing hidden path 
- Mình nhận lại được console và 1 đống error 500 
- Vào check thử lại gặp lỗi quen 

![Alt text](<../image/59.1.png>)
![Alt text](<../image/59.2.png>)

- Nhưng lỗi này có 1 điều kiện là phải có path traversal để lấy thông tin thêm từ file server
- Và không ngờ nó bị ở thẳng đường dẫn luôn :v 

![Alt text](<../image/59.3.png>)

- Theo lời giải ở hacktrick bạn cần lấy những thông tin trong đường dẫn họ đã cung cấp 
![Alt text](<../image/59.4.png>)
- Có 2 lưu ý: username là root chứ không phải cookiehanhoan (mình bị lừa khá lâu vì không check /proc/self/environ)
![Alt text](<../image/59.5.png>)
- Cái private_bits thứ 2 nhớ cộng cả /proc/sys/kernel/random/boot_id + /proc/self/cgroup (file này lấy dòng đầu tiên và chạy code .strip().rpartition("/")[2])
- Bạn sẽ nhận được 1 cái pin code và thành công chạy code python trong cửa sổ console với pin đúng 
![Alt text](<../image/59.6.png>)

- Nhưng không có gì trong file /flag.txt cả ?? 1 là nếu chỉ để flag.txt hoàn toàn dùng 1 lỗi path traversal đọc 
- Cũng có thể ai đó đã báo thủ 

#hackerga2101: