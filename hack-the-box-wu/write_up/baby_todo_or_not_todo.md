- Tiêu đề: baby todo or not todo
- Nội dung: broken access control

- Có thể nói là đang làm bừa tự dưng ra flag :v
- File routes.py có định nghĩa thêm 1 vài route mà tính năng web không cung cấp

![Alt text](<../image/24.1.png>)

- Và ứng với /list/all là query đến database lấy * từ bảng todos

![Alt text](<../image/24.2.png>)

- Thì khi mình thử để xem có access được vào route này không thì hiện flag luôn :v 

![Alt text](<../image/24.3.png>)

- Lỗi do không xác thực quyền từ secrets à ? 

#hackerga2101: