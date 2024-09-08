- Tiêu đề: jscalc
- Nội dung: Inject code nodejs

- Một bài khá ez về việc untrusted data rơi vào hàm eval 
- Hàm eval và đầu vào như sau 
![Alt text](<../image/17.2.png>)

![Alt text](<../image/17.3.png>)

- Require fs đọc local file

![Alt text](<../image/17.1.png>)

- Lụm cờ thôi

![Alt text](<../image/17.4.png>)

#hackerga2101:
- Nếu bạn muốn chạy lệnh hệ thống thì dùng require('child_process').exec('cat /flag.txt') nhưng phải thêm code callback để xử lý bất đồng bộ nếu không kết quả sẽ là object object 