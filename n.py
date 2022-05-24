from bs4 import BeautifulSoup
import requests
url='https://dtf.ru/'
def get_news(url):
     response=requests.get(url)
     print(response.text)
     soup=BeautifulSoup(response.text,'html.parser')
     news=soup.find_all('p',class_='<div class="igx54605 sqq54605 jrn54605 xip54605 yzi54605" style="--offset-top:8761.03px;"><div class="hpu400d6 lwl400d6"><div data-id="5" class="propaganda" id="propaganda_1063"></div> <div class="hiv4daba vtf4daba"><a href="/ad" data-gtm="Buy ads — Banner 300x500 — Clicked" class="pimbc40c lszbc40c"><span>Реклама на DTF</span></a> <a href="/plus" data-gtm="Disable ads offer — Banner 300x500 — Clicked" class="yyeff39c"><span>Отключить рекламу</span></a></div></div></div>')
for el in news:
    print(el.find('span').text)
get_news(url)
for i in range(2,11):
    get_news('https://dtf.ru/'+str(i))
print('hello from lesson')