from bs4 import BeautifulSoup
import urllib.request as req

res=req.urlopen('https://www.kku.ac.kr/mbshome/mbs/wwwkr/index.do')

soup=BeautifulSoup(res,'html.parser')


def head():
    a=[]
    
    for i in soup.find_all(class_="visual_stit"):
        a.append(i.get_text().strip()[0:50])
    return a

def body():
    a=[]

    for i in soup.find_all(class_="visual_txt"):
        a.append(i.get_text().strip())
    return a

for i in soup.find_all(class_="visual_txt"):
    print(i.find('a')['href'])