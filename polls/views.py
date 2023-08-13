from ftplib import all_errors
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.http import Http404
from django import forms
from django.contrib.auth import logout as loogut
import os, csv, math
from bs4 import BeautifulSoup
import urllib.request as req

class UploadFileForm(forms.Form):
    file=forms.FileField()

UPLOAD_DIR = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'

def index(request):
    return render(request, 'polls/index.html')

def mypage(request):
    context={csvreading(request)}
    
    return render(request, 'polls/mypage.html', context)

def add_session(request):
    name=request.POST["productname"]
    price=request.POST["price"]
    product={"name":name,"price":price}

    productlist=[]

    productlist.append(product)
    request.session["shop"]=productlist

    context={}
    context['products']=request.session["shop"]


def handle_uploaded_file(f, request):
    path=os.path.join(UPLOAD_DIR + str(request.session.session_key)+'.csv')
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def test1(request):
    request.session["head"]=head()
    request.session["body"]=body()
    request.session["link"]=link()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        request.session["checklist"]=MaEs2017,MaSe2017,KUinsung2017,GiGyo2017,lang2017,soct2017,scnc2017,art2017,mixed2017,actual2017,career2017,core2017
        context={}
        context['checklist']=request.session["checklist"]
        print(request.session.session_key)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'], request)
            grade=csvreading(request)
            print(grade)
            with open(UPLOAD_DIR+'종합강의시간표내역(학부).CSV') as file:
                reader=csv.reader(file, delimiter=',')
                timetable=[]
                for row in reader:
                    try:
                        if(row[10] == " 컴퓨터공학과, 컴퓨터공학전공, 소프트웨어전공, 컴퓨터공학과"):
                            row[1]=int(row[1])
                            row[9]=int(float(row[9]))
                            if(row[1] == grade[-1][14] and row[3] == '전필'):
                                grade[-1][15]=1

                            if(row[1] == grade[-1][14] and row[3] == '전선'):
                                grade[-1][16]=1
                            timetable.append(row)
                    except:
                        pass
            nul=[]
            request.session["nul"]=nul
            request.session["grade"]=grade
            context['gradelists']=request.session["grade"]
            context['nul']=request.session['nul']
            context['timetb']=request.session["time"]
            context['head']=request.session['head']
            context['body']=request.session['body']
            context['link']=request.session['link']
            delete(request)
            return render(request, 'polls/mypage.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'polls/test1.html', {'form': form})

def test3(request):
    context={csvreading(request)}
    return render(request, 'polls/test3.html', context)
    
def delete(request):
    os.remove(os.path.join(UPLOAD_DIR + str(request.session.session_key) +'.csv'))

def csvreading(request):
    MaEs=0
    MaSe=0
    KUinsung=0
    GiGyo=0
    lang=0
    soct=0
    scnc=0
    art=0
    mixed=0
    actual=0
    career=0
    core=0
    subSum=0
    allSum=0
    year=0
    with open(UPLOAD_DIR+str(request.session.session_key)+'.csv') as file:
        reader=csv.reader(file, delimiter=',')
        gradelist=[]
        for row in reader:
            try:
                if row[0] == '학 번':
                    year=int(row[9])
                
                if row[4] == "총 취득학점 :":
                    print(row)
                    allSum=int(float(row[5]))
                if(row[0] in ('2017','2018','2019','2020','2021','2022')):
                    gradelist.append(row)
                    if(row[3] in MaEs2017):
                        MaEs+=int(row[5])
                    elif(row[3] in MaSe2017):
                        MaSe+=int(row[5])
                    elif(row[3] in KUinsung2017):
                        KUinsung+=int(row[5])
                    elif(row[3] in GiGyo2017):
                        GiGyo+=int(row[5])
                    elif(row[3] in lang2017):
                        lang=2
                    elif(row[3] in soct2017):
                        soct=2
                    elif(row[3] in scnc2017):
                        scnc=2
                    elif(row[3] in art2017):
                        art=2
                    elif(row[3] in mixed2017):
                        mixed=2
                    elif(row[3] in actual2017):
                        actual+=int(row[5])
                    elif(row[3] in career2017):
                        career+=int(row[5])
                    elif(row[3] in core2017):
                        core+=int(row[5])
            except:
                pass
        subSum=lang+soct+scnc+art+mixed
        
    timelist=[MaEs, MaSe, KUinsung,GiGyo,lang,soct,scnc,art,mixed,actual,career,core,subSum,allSum,year,0,0]
    
    gradelist.append(timelist)
    return gradelist
res=req.urlopen('https://www.kku.ac.kr/mbshome/mbs/wwwkr/index.do')

soup=BeautifulSoup(res,'html.parser')


def head():
    a=[]
    
    for i in soup.find_all(class_="visual_stit"):
        a.append(i.get_text().strip())
    return a

def body():
    a=[]

    for i in soup.find_all(class_="visual_txt"):
        a.append(i.get_text().strip()[0:90]+'...')
    return a

def link():
    a=[]
    for i in soup.find_all(class_="visual_txt"):
        a.append('https://www.kku.ac.kr'+i.find('a')['href'])
    return a

MaEs2017=['NDFA57519','NDFA54817','NDFA24338']
MaSe2017=['NDDA48003','NDDA11820','NDDA14393','NDDA14465','NDDA48004','NDDA15050','NDDA50341',
        'NDDA14382','NDDA13692','NDDA14448','NDDA52502','NDDA57518','NDDA50346','NDDA46040',
        'NDDA14514','NDDA53985','NDDA56032','NDDA14446','NDDA14444','NDDA24429','NDDA52508',
        'NDDA54361','NDDA56590','NDDA12075','NDDA56031','NDGE14465','NDGE14393','NDGE11820','NDGE14419','NDGE21122','NDGE14570','NDGE48003','NDGE15050','NDGE50341','NDGE48004','NDGE59586','NDGE14382','NDGE56032','NDGE14448','NDGE53985','NDGE50346','NDGE54361','NDGE14514','NDGE57518','NDGE14446','NDGE39602','NDGE56030','NDGE52508','NDGE46040','NDGE24429','NDGE56572','NDGE12075','NDGE56031']
KUinsung2017=['BKSA58101','BKSA58102','BKSA10922','BKSA58103','BKSA58105','BKSA58104','BKSA58108','BKSA58107','BKSA58106']
GiGyo2017=['BKSA49491','BKSA58232','BKSA58233','BKSA53699','BKSA53700','BKSA58109','BKSA51431',
        'BKSA51432','BKSA58110','BKSA58112','BKSA58113','BKSA56558']
lang2017=['BKSA53714','BKSA54946','BKSA54938','BKSA54939','BKSA46965','BKSA46966','BKSA58226',
        'BKSA58227','BKSA54944','BKSA54945','BKSA54942','BKSA54943','BKSA54940','BKSA54941',
        'BKSA58230','BKSA58231','BKSA58152','BKSA52788','BKSA48172','BKSA11006','BKSA51430',
        'BKSA58154','BKSA58158','BKSA11028','BKSA46712','BKSA39813','BKSA11049','BKSA49983',
        'BKSA58156','BKSA58219','BKSA46814','BKSA11168','BKSA58157','BKSA49630','BKSA04085',
        'BKSA50187','BKSA13364','BKSA12943','BKSA58160','BKSA58164','BKSA58149','BKSA58161',
        'BKSA58155','BKSA58162','BKSA51421','BKSA51422','BKSA45233','BKSA53732','BKSA04745',
        'BKSA04746','BKSA58165','BKSA58163','BKSA58147','BKSA58159']
soct2017=['BKSA46142','BKSA58166','BKSA58175','BKSA58172','BKSA58167','BKSA53720','BKSA52781',
        'BKSA27965','BKSA58168','BKSA58176','BKSA53728','BKSA39826','BKSA58177','BKSA52782',
        'BKSA55127','BKSA53724','BKSA51446','BKSA58178','BKSA53727','BKSA11192','BKSA58174',
        'BKSA11223','BKSA58169','BKSA58179','BKSA11247','BKSA55245','BKSA53723','BKSA58180',
        'BKSA51447','BKSA58170','BKSA46874','BKSA53726','BKSA56961','BKSA44199','BKSA58171']
scnc2017=['BKSA58182','BKSA58183','BKSA51453','BKSA54961','BKSA13630','BKSA50338','BKSA51595',
        'BKSA11145','BKSA11101','BKSA58185','BKSA58220','BKSA58184','BKSA58186','BKSA54347',
        'BKSA54960','BKSA55148','BKSA52777','BKSA56960','BKSA52893','BKSA51459','BKSA53735',
        'BKSA11415','BKSA53733','BKSA54346','BKSA53734','BKSA51457','BKSA58187','BKSA58188',
        'BKSA58189','BKSA58193','BKSA58192','BKSA58190','BKSA58191','BKSA58194']
art2017=['BKSA58205','BKSA51463','BKSA58197','BKSA58198','BKSA58202','BKSA39837','BKSA11021',
        'BKSA53747','BKSA53746','BKSA53749','BKSA58195','BKSA58196','BKSA54360','BKSA58228',
        'BKSA58229','BKSA48185','BKSA53745','BKSA11137','BKSA58199','BKSA11156','BKSA11219',
        'BKSA58207','BKSA58208','BKSA53742','BKSA11231','BKSA51454','BKSA58203','BKSA58200',
        'BKSA53744','BKSA53743','BKSA58204','BKSA53751','BKSA58201','BKSA51469','BKSA51466']
mixed2017=['BKSA58216','BKSA58210','BKSA58213','BKSA58211','BKSA58217','BKSA58212','BKSA58218','BKSA58215','BKSA58214']
actual2017=['BKSA58114']
career2017=['BKSA58116','BKSA58120','BKSA56134','BKSA56849','BKSA58117','BKSA58118','BKSA55147','BKSA45293','BKSA58119','BKSA58145']
core2017=['BKSA15891','BKSA13682','BKSA58133']


