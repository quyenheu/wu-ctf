- tiêu đề : web3 

- FACT : bài này mình không thích tẹo nèo :> bắt bruteforce 57^4 kí tự chịu luôn , và làm mình mất thời gian vch đi tìm cách khai thác như làm thực tế rõ khổ 

- trước tiên là vào view page đã 

![Alt text](<./img/3.1.png>)

- lại là trang tĩnh chán qué è
- vào view cookie mình nhận được 1 cái jwt 

![Alt text](<./img/3.2.png>)

- và đem đi dịch thử 

![Alt text](<./img/3.3.png>)

- mình đã thử đổi guest thành admin rồi mà không không bypass được vì rõ ràng cái quan trọng là signature 
- thui mình nói luôn signature là pctf chứ quét lại lâu vch
- ae quay lại đổi cái signature là sửa ở cookie là được nhe
- à lưu ý xíu là nó có cái exp tức jwt này có hạn sử dụng nha :v nên lúc nào làm thì load lại lấy cái jwt mới 

#hackerga2101: bài này hơi chán nha :> 
- vì mình không nghĩ là phải bruteforce nhiều vậy (cùng lắm thì signature trong common wordlist là đã ổn rồi)
- làm mình lạc lối đi tìm hướng 