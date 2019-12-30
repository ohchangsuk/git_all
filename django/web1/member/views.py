from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
# Create your views here.


cursor= connection.cursor()



@csrf_exempt #post로 값을 전달 받는 곳은 필수 
def join1(request):
    if request.method =='GET':
        return render(request, "member/join1.html")


def list(request):
    sql = "SELECT * FROM MEMBER ORDER BY ID ASC"
    cursor.execute(sql)#sql문 실행
    data = cursor.fetchall() #결과값을 가져옴
    print(type(data))#list
    print(data)# [(1,2,3,4,5),(),()]

    #list.html을 표시하기 전에
    #list 변수에 data값을, title 변수에 "회원목록" 문자를
    return render(request, 'member/list.html',
    {"list":data, "title":"회원목록"})

def index(request):
    #return HttpResponse("index page <hr />")
    return render(request, "member/index.html")

@csrf_exempt
def login(request):
    if request.method =='GET':
        return render(request, "member/login.html")
    elif request.method== 'POST':
        id = request.POST['id']# HTML에서 넘어온 값 받기    
        pw = request.POST['pw']
        ar=[id, pw]#2개로 각각 왔는데 리스트로 만들어서 관리하기 편하게 
        print(ar)
        #DB에 추가함



        #크롬에서 127.0.0.1:8000/member/index 엔터키를 
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