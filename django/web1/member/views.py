from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.contrib.auth.models import User
from django.contrib.auth import authenticate as auth1
from django.contrib.auth import login as login1
from django.contrib.auth import logout as logout1
# Create your views here.
from.models import table2
from django.db.models import Sum, Max, Min, Count, Avg
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from matplotlib import font_manager, rc

cursor= connection.cursor()



def graph(request):


    sum_eng= list(table2.object.values('classroom').annotate(sum_eng=Sum('eng')))
    print('1', sum_eng, type(sum_eng))

    x=[sum_eng[0]['classroom'],sum_eng[1]['classroom'],sum_eng[2]['classroom'],sum_eng[3]['classroom']]
    y=[sum_eng[0]['sum_eng'],sum_eng[1]['sum_eng'],sum_eng[2]['sum_eng'],sum_eng[3]['sum_eng']]
    #폰트 읽기
    font_name = font_manager.FontProperties(fname='c:/windows/fonts/malgun.ttf').get_name()
    #폰트 적용
    rc('font', family=font_name)

    plt.bar(x,y)
    plt.title('ages&person')
    plt.xlabel('반')
    plt.ylabel('영어합계점수')


    plt.draw()#안보이게 그림을 캡쳐
    img=io.BytesIO()
    plt.savefig(img, format='png')
    img_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
#########################################################################################################################
    avg_class=table2.object.values('classroom').annotate(Avg('kor'), Avg('eng'), Avg('math'))


    df = pd.DataFrame(avg_class)
    df = df.set_index('classroom')
    print(df)
    df.plot(kind='bar')
        #plt.show()#표시
    plt.draw()#안보이게 그림을 캡쳐
    img=io.BytesIO()
    plt.savefig(img, format='png')
    img_url1 = base64.b64encode(img.getvalue()).decode()
    plt.close()


    return render(request, 'member/graph.html', {'graph1':'data:;base64,{}'.format(img_url), 'graph2':'data:;base64,{}'.format(img_url1)})

'''
    #select sum('kor')from member_table2
    sum_kor = table2.object.aggregate(Sum('kor'))
    print(sum_kor)#"kor__sum"


    #select sum('kor') as sum1 from member_table2
    sum_kor = table2.object.aggregate(sum1=Sum('kor'))
    print(sum_kor)
    
    #where classroom=102
    sum_kor = table2.object.filter(classroom='102').aggregate(sum1=Sum('kor'))
    print(sum_kor)
    
    #select sum('kor') from member_table2
    #where kor > 10
    # >gt, >=gte, <it, <=ite
    
    sum_kor = table2.object.filter(kor__gt=10).aggregate(sum1=Sum('kor'))
    print(sum_kor)


    #select SUM('kor')sum1, SUM('eng') sum2, SUM('math')sum3
    #from member_table2
    #group by classroom

    sum_kor=table2.object.values('classroom').annotate(sum1=Sum('kor'), sum2=Sum('eng'),sum3=Sum('math'))
    print(sum_kor)
    print(sum_kor.query)

    df = pd.DataFrame(sum_kor)
    df = df.set_index('classroom')
    print(df)
    df.plot(kind='bar')



    x=['kor','eng', 'math']
    y=[3,3,4]'''
 
################################################################################################################
'''#폰트 읽기
    font_name = font_manager.FontProperties(fname='c:/windows/fonts/malgun.ttf').get_name()
    #폰트 적용
    rc('font', family=font_name)

    plt.bar(x,y)
    plt.title('ages&person')
    plt.xlabel('나이')
    plt.ylabel('숫자')

    #plt.show()#표시
    plt.draw()#안보이게 그림을 캡쳐
    img=io.BytesIO()
    plt.savefig(img, format='png')
    img_url = base64.b64encode(img.getvalue()).decode()
    plt.close()

    return render(request, 'member/graph.html', {'graph1':'data:;base64,{}'.format(img_url)}) '''
    #<img src='{{graph1}}'/> <= graph.html에서

def dataframe(request):
    #select*from member_table2
    #rows = table2.objects.all()

    # 1, QuerySet > list로변경
    #select no,name,kor from member_table2
    rows= table2.object.all().values('no','name','kor')

    
    print(type(rows))
    #2, list > dataframe으로 변경
    df=pd.DataFrame(rows)
    
    #3, dataframe ->list
    rows1 = df.values.tolist()
    print(type(rows1))
    print(type(df))
    return render(request, 'member/dataframe.html', {'df_table':df.to_html(), 'list':rows, 'list1':rows1})

def index(request):
    #return HttpResponse("index page <hr />")
    return render(request, "member/index.html")
    
@csrf_exempt
def delete(request):
    if request.method=='GET' or request.method=='POST':
        ar=[request.session['userid']]
        sql="DELETE FROM MEMBER WHERE ID = %s"    
        cursor.execute(sql, ar)

        return redirect('/member/logout')
@csrf_exempt
def edit(request):
    if request.method =='GET':
        ar=[request.session['userid']]

        sql = '''
            SELECT * FROM MEMBER WHERE ID=%s
        '''

        cursor.execute(sql, ar)
        data=cursor.fetchone()
        print(data)
        return render(request, "member/edit.html",{"one":data})
    elif request.method == 'POST':
        ar = [
            request.POST['name'],
            request.POST['age'],
            request.POST['id'],
        ]
        
        sql='''
            UPDATE MEMBER SET NAME=%s, AGE=%s
            WHERE ID=%s
        '''
        cursor.execute(sql, ar)

        return redirect("/member/index")

        # HTML에서 넘어온 값 받기  

@csrf_exempt
def join1(request):
    if request.method =='GET':#post로 값을 전달 받는 곳은 필수 
        return render(request, "member/join1.html")
    elif request.method== 'POST':
         return render(request, "member/join1.html")
    

def list1(request):
    sql = "SELECT * FROM MEMBER ORDER BY ID ASC" #오름차순 or 내림차순
    cursor.execute(sql)#sql문 실행
    data = cursor.fetchall() #결과값을 가져옴
    print(type(data))#list
    print(data)# [(1,2,3,4,5),(),()]

    #list.html을 표시하기 전에
    #list 변수에 data값을, title 변수에 "회원목록" 문자를
    return render(request, 'member/list.html',
    {"list":data, "title":"회원목록"})


@csrf_exempt
def login(request):
    if request.method =='GET':
        return render(request, "member/login.html")
    elif request.method== 'POST':
        # HTML에서 넘어온 값 받기    
        ar = [request.POST['id'], request.POST['pw']]
        print(ar)

        
        #DB에 추가함 id는 id로 받고 pw는 밑에 pw=%s에 넣는다 그리고 난 후 아이디와 이름을 골라서 화면에뿌려주는것. 로그인
        sql="SELECT * FROM MEMBER WHERE ID=%s AND PW=%s"

        cursor.execute(sql, ar)
       
        data=cursor.fetchone()#한줄 가져 오기 아이디가 한개니깐 중복 되면 데이터 베이스가 엉망이란 소리 이므로.
        print(type(data))
        print(data)

        
        if data:
            request.session['userid']=data[0]
            request.session['username']=data[1]
            return redirect('/member/index')
        

        return redirect('/member/login')


        #크롬에서 127.0.0.1:8000/member/index 엔터키를 
@csrf_exempt #post로 값을 전달 받는 곳은 필수 
def logout(request):
    if request.method =='GET' or request.method == 'POST':
        del request.session['userid']
        del request.session['username']
        return redirect('/member/index')


@csrf_exempt #post로 값을 전달 받는 곳은 필수 
def join(request):
    if request.method =='GET':
        return render(request, "member/join.html")
    elif request.method== 'POST':
        id = request.POST['id']# HTML에서 넘어온 값 받기
        na = request.POST['name']
        ag = request.POST['age']
        pw = request.POST['pw']

        ar=[id, na, ag, pw]#4개로 각각 왔는데 리스트로 만들어서 관리하기 편하게 
        print(ar)
        #DB에 추가함

        
        sql='''        
        INSERT INTO MEMBER (ID,NAME,AGE,PW,JOINDATE)
        VALUES(%s, %s, %s, %s, SYSDATE)
        '''
        cursor.execute(sql, ar)


        #크롬에서 127.0.0.1:8000/member/index 엔터키를 
        return redirect('/member/index')
@csrf_exempt
def auth_join(request):
    if request.method =="GET":
        return render(request,'member/auth_join.html')
    elif request.method=='POST':
        id = request.POST['username']
        pw = request.POST['password']
        na = request.POST['first_name']
        em = request.POST['email']

        obj = User.objects.create_user(
            
            username=id,
            password=pw,
            first_name=na,
            email=em
            )
        obj.save()

        return redirect('/member/auth_index')


@csrf_exempt
def auth_index(request):
    if request.method =="GET":
        return render(request,'member/auth_index.html')
    elif request.method=='POST':
        return redirect('/member/auth_index')

@csrf_exempt
def auth_login(request):
    if request.method =="GET":
        return render(request,'member/auth_login.html')
    elif request.method=='POST':
        id = request.POST['username']
        pw = request.POST['password']
        #db에 인증하기
        obj = auth1(request, username=id, password=pw)

        if obj is not None:
            login1(request,obj) #세션에 추가
        return redirect("/member/auth_index")
@csrf_exempt
def auth_logout(request):
    if request.method =="GET" or request.method=='POST':
        logout1(request) # 세션 초기화 
        return redirect("/member/auth_index")
@csrf_exempt
def auth_edit(request):
    if request.method =="GET":
        if not request.user.is_authenticated:
            return redirect('/memeber/auth_login')

        obj=User.objects.get(username=request.user)
        return render(request, 'member/auth_edit.html', {'obj':obj})
    elif request.method=='POST':
        id = request.POST['username']
        na = request.POST['first_name']
        em = request.POST['email']

        obj=User.objects.get(username=id)
        obj.first_name =na
        obj.email=em
        obj.save()
        return redirect('/member/auth_index')
@csrf_exempt
def auth_pw(request):
    if request.method =="GET":
        if not request.user.is_authenticated:
            return redirect('/memeber/auth_login')

        return render(request, 'member/auth_pw.html')

    elif request.method=='POST':
        pw=request.POST['pw']
        pw1=request.POST['pw1']
        obj=auth1(request, username=request.user, password=pw)
        if obj:
            obj.set_password(pw1) #pw1으로 암호변경
            obj.save()
            return redirect('/member/auth_index')
        return redirect('/member/auth_pw')
##############################################################exam_#####################################
#URLS.PY
#EXAM_INSERT
#EXAM_UPDATE
#EXAM_DLELTE
#EXAM_SELECT
def exam_insert(request):
    if request.method =="GET":
        rows=table2.object.all()# select
        return render(request, 'member/exam_insert.html', {'list':rows})

    elif request.method=='POST':
        obj = table2()#obj객체 생성
        obj.name = request.POST['name']
        obj.kor = request.POST['kor']
        obj.eng = request.POST['eng']
        obj.math = request.POST['math']
        obj.classroom = request.POST['classroom']
        obj.save()
        return redirect('/member/exam_insert')

def exam_update(request):
        if request.method=='GET':
            n = request.GET.get('no', 0)
            row = table2.object.get(no=n)
            return render(request, 'member/exam_update.html', {'one':row})
        elif request.method=='POST':
                n=request.POST['no']
                obj = table2.object.get(no=n)#obj객체 가져옴
                obj.name = request.POST['name']# 변수의 값
                obj.kor = request.POST['kor']
                obj.eng = request.POST['eng']
                obj.math = request.POST['math']
                obj.save() #저장하기 수행

                #UPDATE BOARD_TABLE2 SET
                # NAME=%s, KOR=%s, ENG = %s, MATH=%s WHERE=%s
                return redirect('/member/exam_insert')  

def exam_delete(request):
    if request.method =="GET":
        n = request.GET.get('no',0)
            #SQL : SELECT * FROM BOARD_TABEL2 WHERE NO=%s
        row = table2.object.get(no=n)
        row.delete() #삭제

        return redirect('/member/exam_insert')

def exam_select(request):
    
    txt=request.GET.get('txt','')
    page = int(request.GET.get('page', 1))
    
    if txt=='':
        #select*from member_table2 <--- >>범위잡을때 쓰는거>> limit 0, 10

        list = table2.object.all()[page*10-10:page*10]
        #select count(*) from member_table12
        cnt = table2.object.all().count()
        tot = (cnt-1)//10+1
    else: #검색어가 있는경우
        #select *from member_table2 where name like '%가%'
        list= table2.object.filter(name__contains=txt)[page*10-10:page*10]
        #select count(*) from member_table2 where name like '%가%'
        cnt=table2.object.filter(name__contains=txt).count()
        tot = (cnt-1)//10+1


    return render(request, 'member/exam_select.html', {'list':list, 'pages':range(1, tot+1, 1)})

def js_index(request):
    return render(request, 'member/js_index.html')
def js_chart(request):
    str = '100, 200, 300, 400, 300, 200, 100'
    return render(request, 'member/js_chart.html', {'str':str})

































'''
 if request.method=='GET'
        n=request.session['no'] # 8, 5, 3
        print(n)
        rows = table2.object.filter(no__in=n)
            #"SELECT * FROM BOARD_TABLE2 WHERE NO=8 OR NO =5 OR NO=3"
            #"SELECT * FROM BOARD_TABLE2 WHERE NO IN (8,5,3)"       
            #"SELECT * FROM BOARD_TABLE2 WHERE NO=8 OR NO =5 OR NO=3"

        return render(request, 'member/exam_insert.html', {'list':rows})

    elif request.method=='POST':
        no=request.POST.getlist('no[]')
        name=request.POST.getlist('name[]')
        kor=request.POST.getlist('kor[]')
        eng=request.POST.getlist('eng[]')
        math=request.POST.getlist('math[]')
        objs=[]

        for i in range(0, len(no), 1):
            obj = table2.object.get(no=no[i])
            obj.name = name[i]
            obj.kor = kor[i]
            obj.eng = eng[i]
            obj.math = math[i]
            objs.append(obj)
            return redirect("/member/exam_insert")
'''
'''def exam_select(request):
no= request.Get.get('no',0)
SELECT SUM(math) FROM MEMBER_TABLE2
list = table2.object.aggregate(sum('math'))

SELECT NO, NAME FROM MEMER_TABLE2
list = table2.object.all().values(['no','name'])

SELECT * FROM MEMBER_TABLE2 ORDER BU NAME ASC
list = table2.object.all().order_by('name')
list = table2.object.raw('SELECT * FROM MEMBER_TABLE2 ORDER BU NAME ASC')'''

'반 별 국어, 영어, 수학 합계'


