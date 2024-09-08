- Tiêu đề: petpet rcbee
- Nội dung: RCE lib PIL 

- Đây là 1 chall về CVE-2018-16509 Artifex Ghostscript cho phép RCE 

![Alt text](<../image/23.1.png>)

- Sau khi view qua source thì mình không thấy có lỗi gì nên đã đi research thử các thư viện và hàm
- Mình tìm 1 được 1 bài viết khá cụ thể về lỗi trên và follow theo 

![Alt text](<../image/23.7.png>)

- Cụ thể là việc convert ở trong thư viện trên sẽ phát sinh ra lỗi img = Image.open(img_path)

![Alt text](<../image/23.2.png>)

- Mình tìm thấy documents root trong file config
- Tiến hành khai thác với việc thử tạo 1 file txt

![Alt text](<../image/23.3.png>)
![Alt text](<../image/23.4.png>)

- Thành công truy cập file exp.txt 
- Đổi lại lệnh để cat flag thôi 

![Alt text](<../image/23.5.png>)
![Alt text](<../image/23.6.png>)

#hackerga2101: 
- Link follow: https://github.com/farisv/PIL-RCE-Ghostscript-CVE-2018-16509

