from webbot import Browser 
import time
import re
from bs4 import BeautifulSoup

def init():

    user = "victor.mendes"
    passwd = open("mypasswd").read()
    
    # data = webot(user,passwd)
    data = open("demofile2.html").read()

    resolveHTML(data)

def resolveHTML(html):

    soup = BeautifulSoup(html, 'html.parser')

    falta = soup.find_all('table')[0].find_all('div')[1].find('strong').contents[0]
    total = soup.find_all('table')[0].find_all('div')[1].find('small').contents[0]
    print(falta,total)

    falta = soup.find_all('table')[1].find_all('div')[1].find('strong').contents[0]
    total = soup.find_all('table')[1].find_all('div')[1].find('small').contents[0]
    print(falta,total)

    falta = soup.find_all('table')[2].find_all('div')[1].find('strong').contents[0]
    total = soup.find_all('table')[2].find_all('div')[1].find('small').contents[0]
    print(falta,total)

    falta = soup.find_all('table')[3].find_all('div')[1].find('strong').contents[0]
    total = soup.find_all('table')[3].find_all('div')[1].find('small').contents[0]
    print(falta,total)

    falta = soup.find_all('table')[4].find_all('div')[1].find('strong').contents[0]
    total = soup.find_all('table')[4].find_all('div')[1].find('small').contents[0]
    print(falta,total)

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