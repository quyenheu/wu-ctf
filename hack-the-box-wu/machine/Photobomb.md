- Tiêu đề: Photobomb
- Nội dung: ?

- Trước tiên mình nmap thu được 2 port 22 và 80 
- Mình viết lại file /etc/hosts để phân giải tên miền và truy cập vào 
- Vẫn là 1 trang không có mấy tính năng. Sau khi fuzzing mình thấy được một số endpoint như /printer nhưng khi truy cập thì sẽ cần authen 
- Lọ Mọ trong file Photobomb.js mình chú ý đến 1 đường dẫn 

![Alt text](<../image_machine/2.5.png>)

- Đường dẫn trên đang để dạng user:pass nên mình thử login với thông tin trên và thành công vào được trang printer
- Trang này cho phép mình tải ảnh và mình đã thử được payload cmdi time based trong đó 

![Alt text](<../image_machine/2.1.png>)

- Sửa lại lệnh để lấy reverse về máy và cat file user.txt 


![Alt text](<../image_machine/2.2.png>)

![Alt text](<../image_machine/2.3.png>)

- Tiếp theo mình get 1 file linpeas về và chạy thử 

![Alt text](<../image_machine/2.4.png>)

- File /opt/cleanup.sh đang được chạy dưới quyền root NOPASSWD
- Tìm hiểu kĩ hơn về file thì nó có nhận SETENV là cách sửa biến mỗi trường hiện tại
- Lệnh find đang được truy vấn theo biến môi trường nên mình sẽ lợi dụng lệnh đó để leo quyền 
- Ý tưởng là sửa lại lệnh find để nó chạy bash và định nghĩa trong 1 đường dẫn mới 

![Alt text](<../image_machine/2.6.png>)

- Mình chạy SUDO $PATH=$PWD:$PATH /opt/cleanup.sh để kích hoạt quyền root và định nghĩa lại path env thành thư mục hiện tại (chứa find mình định nghĩa)
- Giờ lệnh find sẽ được chạy dưới quyền root và mở 1 cái bash (mình echo -e'#!/bin/bash\nbash' > find)

#hackerga2101: