- Tiêu đề: baby website rick
- Nội dung: pickle serialization python 

- Pickle sẽ có 4 loại protocol khác nhau phù hợp với từng version py
- Và trong bài này cookie của bài khi decode ra sẽ là dạng pickle với protocol = 0 

- Với .anti_pickle_resum là 1 object (khi bạn debug thử data sẽ nhận ra)
- Tiếp đó mình gen lại mã để khai thác 

![Alt text](<../image/32.1.png>)

- Nhưng với payload cPickle thì python3 không còn hỗ trợ 

![Alt text](<../image/32.2.png>)

- Nên hãy gen lại với python2 để có payload chuẩn nhất 

![Alt text](<../image/32.3.png>)

![Alt text](<../image/33.4.png>)

#hackerga2101: 