from webbot import Browser 
import time
import re

def init():

    user = "victor.mendes"
    passwd = open("mypasswd").read()
    
    # data = webot(user,passwd)
    data = open("demofile2.html").read()

    count = data.find("matricula.acdMtrResultado !")
    matriculadas = int(data.count("matricula.acdMtrResultado !"))//2
    for x in range(matriculadas):        
        
        tupla = data[count+185:count+274]
        falta = tupla[:2]
        total = tupla[-3:]
        if falta != 'DF':
            falta = int(re.search(r'\d+', falta).group(0))
            total = int(re.search(r'\d+', total).group(0))
            print(falta,total)

        count = data.find("matricula.acdMtrResultado !",count+1);

def webot(user,passwd):
    web = Browser(False)
    web.go_to("https://midas.unioeste.br/login/#/") 
    time.sleep(5)
    web.type(user, id="login-username") 
    web.type(passwd, id="login-password") 
    web.press(web.Key.ENTER) 
    time.sleep(5)
    web.click('Academus')
    time.sleep(5)
    web.click('Matrículas')
    time.sleep(3)
    data = web.get_page_source()
    web.close_current_tab()
    return data

init()