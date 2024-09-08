- Tiêu đề: Bypass HMAC check
- Nội dung: bypass hàm hash_hmac php to cmdi

- Trước tiên là về hàm hash_hmac. hash_hmac(string $algo, string $data, string $key, bool $binary = false): string
- Ngay trong php.net cũng đã đề cập nếu hash_hmac được dùng với array thì sẽ trả về warming nhưng kết quả của phép tính đó vẫn là false
- Như source hiện lên ở trên web ta có 2 lần hash_hmac vậy hoàn toàn kiểm soát tất cả các biến từ đó cmdi

![Alt text](<../image/61.1.png>)

- Mình tạo lại code php để tạo mã hash_hmac với payload ở trường host 

![Alt text](<../image/61.2.png>)

#hackerga2101: 
- Có một vấn đề là nếu bạn POST bằng burpsuite hay python thì nhất quyết sẽ không có kết quả (hoặc là mình làm sai :v)
