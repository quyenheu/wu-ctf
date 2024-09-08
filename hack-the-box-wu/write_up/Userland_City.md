- Tiêu đề: Userland City
- Nội dung: CVE-2021-3129

- Bài này là CVE-2021-3129 khai thác debug code của lavarel 
- Sau một hồi loay hoay với form login và register thì mình dùng nuclei và phát hiện ra lỗi trên 

![Alt text](<../image/40.1.png>)

![Alt text](<../image/40.2.png>)

- Mình result và follow hướng dẫn phía dưới để làm bài này 
- Git clone và chạy script exploit khá đơn giản 

![Alt text](<../image/40.3.png>)

- Vì không thấy được result in ra của các lệnh nên mình curl ra webhook 

- Và execute được command nên việc lấy flag dễ rồi

![Alt text](<../image/40.4.png>)

#hackerga2101: 
- https://github.com/joshuavanderpoll/CVE-2021-3129
- Link để hiểu về lỗ hổng trên: https://viblo.asia/p/laravel-v842-debug-mode-remote-code-execution-chiem-quyen-dieu-khien-may-thang-ban-dang-code-php-6J3ZgN8PKmB
- Follow link thứ 2 để làm tay nhé :v 