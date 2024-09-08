- Tiêu đề: Phonebook
- Nội dung: LDAP injection 

- Đây là lần đầu mình làm ldap nên cũng khó gọn gàng được (vì làm blackbox nên k biết ldap là đi)

![Alt text](<../image/10.1.png>)

- Mình thử từ sqli đến xss to read localfile, ... không có cách nào hiệu quả 
- Và tra được một vài cách pybass login 

![Alt text](<../image/10.2.png>)

- Thì với ldap login theo kiểu gần giống like trong sql (theo mình hiểu là thế)
- Nên username=*&password=* 

![Alt text](<../image/10.3.png>)

- Bên trong có tính năng search mà không có gì để khai thác 

- Quay ra viết script dump password là có flag 

![Alt text](<../image/10.4.png>)

#hackerga2101: