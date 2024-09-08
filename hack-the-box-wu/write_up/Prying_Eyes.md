- Tiêu đề: Prying Eyes
- Nội dung: imagemagick-convert CVE-2022-44268

- *bài này là lỗi trong thư viện imageagick cũng như các inject thêm param để bypass code - Mình tham khảo nhiều để làm được bài này
- Web có những chức năng cơ bản: login, register, post blog và comment blog 
- Mình đã đọc code toàn bài và phát sinh lỗi chỉ có thể trong hàm convert của thư viện imagemagick 

![Alt text](<../image/46.4.png>)

- Chức năng đoạn code là lấy thông tin từ post request lưu vào các biến title, message, parentId và convertParams - thằng này sẽ chứa tất cả thông tin còn lại khác 3 biến trên 
- Nếu upload 1 ảnh thì sẽ nhận được convert sang .avif và lưu trong /uploads
- Sau khi search vuln trong thư viện trên mình thấy bài giống với CVE-2022-44268 
- Nhưng vấn đề là việc code convert qua dạng .avif sẽ tránh được lỗi ở CVE trên 
- Giờ mình cùng phân tích source của thư viện imagemagick để hiểu cách các tham số được xử lý 

```
attributesMap = new Set([
        'density',
        'background',
        'gravity',
        'quality',
        'blur',
        'rotate',
        'flip'
    ]);
    composeCommand(origin, result) {
        const cmd = [],
            resize = this.resizeFactory();
        for (const attribute of attributesMap) {
            const value = this.options.get(attribute);
            if (value || value === 0) cmd.push(typeof value === 'boolean' ? `-${attribute}` : `-${attribute} ${value}`);
        }
        if (resize) cmd.push(resize);
        cmd.push(origin);
        cmd.push(result);
        return cmd.join(' ').split(' ');
    }

    const origin = this.createOccurrence(this.options.get('srcFormat')),
        result = this.createOccurrence(this.options.get('format')),
        cmd = this.composeCommand(origin, result),
        cp = spawn('convert', cmd),
        store = [];
```

- Có thể thấy thư viện xử lý đang call cmd cơ bản và thực hiện lấy các params từ post request làm option 

```
[
  '-density',    '600',
  '-background', 'none',
  '-gravity',    'Center',
  '-quality',    '75',
  'PNG:-',       'AVIF:-'
]
```
- Kết quả khởi tạo thử 
- Nhưng trong thư viện trên có 1 option là -write 

![Alt text](<../image/46.5.png>)

- Vậy nếu có thể lợi dụng option trên để ghi được file .png thì sẽ khai thác được CVE trên 
- Mình sẽ inject thêm param background để nối dài câu command thêm option ghi file 
- Và nội dung file sẽ được tạo bằng poc mình để bên dưới 
- ./poc.py generate -o poc.png -r flag.txt

![Alt text](<../image/46.3.png>)

- Upload ở 1 chức năng bất kì và truy cập vào lấy ảnh sau khi upload 

![Alt text](<../image/46.2.png>)

- Parse ngược lấy flag 
- ./poc.py parse -i exp.png
- Lấy phần số ở dòng raw profile type và dịch ngược lại 

![Alt text](<../image/46.1.png>)

#hackerga2101: 
- POC: https://github.com/vulhub/vulhub/blob/master/imagemagick/CVE-2022-44268/poc.py
- Link follow: https://www.freebuf.com/articles/web/367929.html