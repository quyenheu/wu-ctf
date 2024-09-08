- Tiêu đề: Cursed Secret Party
- Nội dung: XSS to steal cookie

- Đây là 1 bài xss bypass csp khá hay 
- Trước tiên mình dùng thử tính năng của web. Khi bạn submit thông tin lên 

![Alt text](<../image/21.2.png>)

- Tiếp đó mình đọc source và thấy flow của bài như sau

![Alt text](<../image/21.3.png>)

- Sau khi submit thì sẽ có 1 bot visit check cụ thể là check /admin và /admin_delete

![Alt text](<../image/21.4.png>)

- Nếu user_role === admin thì sẽ gọi hàm lấy dữ liệu trong database và render cùng với admin.html (đương nhiên bot là role admin)

![Alt text](<../image/21.5.png>)

- Hàm lấy dữ liệu select * 

![Alt text](<../image/21.7.png>)

- Mình thấy flag đang được mã hóa JWT trong cookie của con bot khi visit

![Alt text](<../image/21.6.png>)

- Set header policy và csp cho toàn bộ trang
- Vì thấy flag trong cookie và phải bypass qua user_role nên XSS là hợp lý để có được flag 

![Alt text](<../image/21.8.png>)

- Và vì từng làm csp nên mình biết 1 số bên thứ 3 bị lỗi và scrip-src jsdelivr trong bài này bị lỗi 
- Tiếp đó mình tìm cách up 1 file js do mình kiểm soát lên domain cdn.jsdelivr.net 

![Alt text](<../image/21.9.png>)

- Bạn chỉ cần upload 1 file script lên github là tự động có trên cdn.jsdelivr.net theo đường dẫn sau 
+ cdn.jsdelivr.net/gh/{username_github}/{tên_kho}/{tenfile.js}

![Alt text](<../image/21.10.png>)

- Giờ thì inject vào, Thành công lấy được cookie admin

![Alt text](<../image/21.11.png>)

- Decode jwt lấy cờ th

![Alt text](<../image/21.12.png>)

#hackerga2101:
- Ngoài bypass csp dạo đây ctf còn nổi Prototype Pollution
- Link follow: https://sensepost.com/blog/2023/dress-code-the-talk/#bypasses