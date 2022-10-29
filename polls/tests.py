from bs4 import BeautifulSoup
import urllib.request

url='https://www.kku.ac.kr/mbshome/mbs/wwwkr/index.do'
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html, 'html.parser')

for anchor in soup.find_all(class_='sm_mv_slide'):
    print(anchor)

print(len(anchor))