- Tiêu đề: Code get Flag
- Nội dung: code inject bypass blacklist 

- 1 bài khá hay để thoát khỏi vỏ bọc script kiddle 
- Trước giờ ssti mình thường lấy payload trên mạng và hầu như không hiểu rõ payload 

- Trước tiên thì mình cũng debug tùm lum payload ở local nhưng không hiệu quả và tình cờ đọc được 1 bài giải thích payload nên mới hiểu và xây lại 

Payload: print(''.__class__.__base__.__subclasses__()[132].__init__.__globals__['system']('cat /flag.txt'))

- Nhìn có vẻ rất quen thuộc nhưng không vì hầu hết trên mạng là [133] nên sẽ sai với bài này

- Mình follow link dưới bài để làm 
- Trước tiên intruder nên biết có thể dùng ''.__class__.__base__.__subclasses__() Xem danh sách tất cả lớp con của lớp Object trong ứng dụng

![Alt text](<../image/62.1.png>)

- Sau đó tìm class có thể dùng ví dụ class os._wrap_close

![Alt text](<../image/62.2.png>)

- Tiếp đó tìm Phương thức có thể dùng trong class đó. có cả popen và system nhưng blacklist có open nên bỏ popen

![Alt text](<../image/62.3.png>)

- Và lấy cờ thôi 

![Alt text](<../image/62.4.png>)

- Có thể là do mình chưa biết về cách dựng lại payload nên mất khá nhiều thời gian :v Nhưng cũng okela 

#hackerga2101:
- https://viblo.asia/p/server-side-template-injection-vulnerabilities-ssti-cac-lo-hong-ssti-phan-2-qPoL775jLvk
- https://viblo.asia/p/server-side-template-injection-vulnerabilities-ssti-cac-lo-hong-ssti-phan-3-Ny0VGjAYLPA