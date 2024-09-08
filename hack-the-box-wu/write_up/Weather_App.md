- Tiêu đề: Weather App
- Nội dung: SSRF to SQLi (CVE 2018-12116)

- Đây là 1 thử thách whitebox express nodejs 
- Mình đọc source cũng nhanh chóng nhận ra một số lỗi và hướng khai thác nhưng để đánh giá easy như htb thì chịu :v 

![Alt text](<../image/1.1.png>)
![Alt text](<../image/1.2.png>)

- Giao diện sẽ hiển thị thời tiết và địa điểm của bạn (check theo ip)
- Và đó là 1 post request đến api.openweathermap.org

- Đoạn code xử lý như sau: 
![Alt text](<../image/1.3.png>)

- Nhìn là thấy có thể lợi dụng được rồi +1
- Phân tích source tiếp ta thấy một vài đoạn code sau: 
![Alt text](<../image/1.4.png>)

- Chức năng register yêu cầu ip local để đăng ký 

![Alt text](<../image/1.6.png>)

- Và lưu thông tin đăng ký bằng sql nhưng đoạn insert lại dính lỗi SQLi
- Tiếp đó ở chức năng login 

![Alt text](<../image/1.5.png>)

- Nếu bạn login với account admin thì sẽ có được flag 

-> Hướng là SSRF để SQLi update lại account admin theo ý mình 

- Nhưng khó khăn là how to SSRF? vì nó không nhận các headers inject và mình cũng thử với param miner rồi 
![Alt text](<../image/1.8.png>)

- Hướng 1: liệu có XSS để nó thay mình gửi request POST được không 
- XSS thì thực hiện được ở tính năng api kia như sau:
- Bạn hãy tạo 1 domain do mình quản lý xử lý reqest đến theo form dưới đây (mình dùng free của portswigger :v)

![Alt text](<../image/1.7.png>)
- Data hoàn toàn không bị filter 
![Alt text](<../image/1.9.png>)
- Nhưng mình thất bại vì khi thử fetch đến domain hackerga201.request.catcher thì không có request đến 

--> Phải có cách nào để khai thác SSRF khác 
- Sau 1 hồi research thì cũng có 1 CVE khá phù hợp: nó nói nếu bạn encode unicode data cho cái path option thì có thể lừa gửi nhiều request 

![Alt text](<../image/1.10.png>)

- Set up payload inject unicode để thực thi nhiều request với chức năng /api/weather khi nó gửi request lấy thời tiết

![Alt text](<../image/1.11.png>)

- Và thành công cập nhật mật khẩu admin giờ login là ăn cờ thôi 

#hackerga2101:
- Khởi đầu Hackthebox lab easy mà thấy ngộp rồi :>