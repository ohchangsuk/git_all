from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from base64 import b64encode  #이미지 인코딩 해주는 코드(byte매열을 base64로 변경함.)
import pandas as pd
from.models import Table2 # models.py파일의 table2클래스 연결

# Create your views here.
cursor = connection.cursor()#sql수행을 위한 cursor객체

def dataframe(request):
    if request.method == 'GET':
        df = pd.read_sql(
            '''
            SELECT NO, WRITER, HIT, REGDATE FROM BOARD_TABLE1
            
            ''', con=connection)
        print(df)
        print(df['NO'])
        print(type(df))
        return render(request, 'board/dataframe.html', {'df':df.to_html()})

@csrf_exempt
def edit(request):
    if request.method=='GET':
        no = request.GET.get('no',0)


        sql="""
            SELECT NO, TITLE, CONTENT
            FROM BOARD_TABLE1
            WHERE NO=%s
        
         """

        cursor.execute(sql, [no])
        data= cursor.fetchone()
        return render(request, "board/edit.html", {"one":data})

    elif request.method=='POST':
        no =request.POST['no']
        ti =request.POST['title']
        co =request.POST['content']
        arr = [ti, co, no]
        sql='''
                UPDATE BOARD_TABLE1 SET TITLE=%s,
                CONTENT=%s WHERE NO = %s          
            '''
        cursor.execute(sql, arr)
        return redirect("/board/content?no="+no)


#127.0.0.1:8000:/board/delete?no=37
#127.0.0.1:8000:/board/delete
@csrf_exempt
def delete(request):
    if request.method=='GET':
        no = request.GET.get('no',0)# url값이 없으면 0 으로 들어 오게 하게 

        sql = """
            DELETE FROM BOARD_TABLE1
            WHERE NO=%s
            """

        cursor.execute(sql, [no])
        
        return redirect("/board/list")


@csrf_exempt
def content(request):
    if request.method == "GET":
        no = request.GET.get('no', 0) #POST에서 name 받는것 처럼 get에서 받는것

        if no == 0 :
            return redirect("/board/list")#<a href 와 같음

        if request.session['hit']== 1 :
        # 조회수 1증가 시킴
            sql = """
                    UPDATE BOARD_TABLE1 SET HIT = HIT+1
                    WHERE NO=%s
            """
            cursor.execute(sql, [no])
            request.session['hit'] = 0



        #이전글 가져오기
        sql = '''   SELECT NVL(MAX(NO), 0)
                    FROM BOARD_TABLE1
                    WHERE NO < %s
        '''
        cursor.execute(sql, [no])
        prev = cursor.fetchone()

        #다음글 가져오기            
        sql = '''  SELECT NVL(MIN(NO), 0)
                FROM BOARD_TABLE1
                WHERE NO > %s
        '''
        cursor.execute(sql, [no])
        nxt = cursor.fetchone()

#게시글 가져오기

        sql = """
            SELECT 
                NO, TITLE, CONTENT, WRITER, HIT, 
                TO_CHAR(REGDATE, 'YYYY-MM-DD HH:MI:SS'),
                IMG
            FROM 
                BOARD_TABLE1
            WHERE
                NO=%s
    
        """
        cursor.execute(sql, [no])
        data = cursor.fetchone()# ()튜플로 되어 있음...............;ㅎ;
        print(data)#db에서 받은 게시물 1개의 정보 출력
        if data[6]: #db에 blob로 있는 경우
            img = data[6].read() # 바이트배열을 img에 넣음.
            img64=b64encode(img).decode("utf-8")
        
        else :# 없는경우
            file = open('./static/img/no_detail_img.gif', 'rb')
            img = file.read()
            img64 = b64encode(img).decode("utf-8")

        #print(no)
        return render(request, 'board/content.html', {"one":data, "image":img64, "prev":prev[0], "next":nxt[0]}) 
    

@csrf_exempt
def list(request):
    if request.method == "GET":

        request.session['hit'] = 1 #세션에 hit + 1

        #DESC<<오름차순(최신글이 먼저 와야 하므로)
        sql = """
                SELECT 
                    NO,TITLE, WRITER, HIT, TO_CHAR(REGDATE, 'YYYY-MM-DD HH:MI:SS') 
                FROM 
                    BOARD_TABLE1
                ORDER BY NO DESC
        """
        cursor.execute(sql)
        data = cursor.fetchall()
        print(type(data))


        return render(request, 'board/list.html', {"list":data} )


@csrf_exempt
def write(request):
    if request.method=='GET':
        return render(request, 'board/write.html' )
    elif request.method=='POST':
        
        tmp=None
        if 'img' in request.FILES:
            img = request.FILES['img']
            tmp = img.read()

            print(tmp,type(tmp))
                        
        arr=[
            request.POST['title'],
            request.POST['content'],
            request.POST['writer'],     
            tmp   # 이미지를 byte[]로 변경
            
        ]
        print(tmp,type(tmp))
        try:
        #print(arr)
        
            sql = """
            INSERT INTO BOARD_TABLE1(TITLE, CONTENT, WRITER, IMG, HIT, REGDATE) VALUES(%s, %s, %s, %s, 234, SYSDATE)
            """


            cursor.execute(sql, arr)

        except Exception as e:
            print(e)


        return redirect("/board/list")#<a href 와 같음
        

def t2_insert(request):
    if request.method=='GET':
        return render(request, 'board/t2_insert.html')
    elif request.method=='POST':
        obj = Table2()#obj객체 생성
        obj.name = request.POST['name']# 변수의 값
        obj.kor = request.POST['kor']
        obj.eng = request.POST['eng']
        obj.math = request.POST['math']
        obj.save() #저장하기 수행
        
        return redirect('/board/t2_list')

@csrf_exempt
def t2_list(request):
    if request.method=='GET':
        rows=Table2.object.all()# select
        print(rows)
        print(type(rows))
        return render(request, 'board/t2_list.html', {'list':rows})
    elif request.method=='POST':
        pass
        return redirect('/board/t2_list')
@csrf_exempt
def t2_delete(request):
        if request.method=='GET':
            n = request.GET.get('no',0)
                #SQL : SELECT * FROM BOARD_TABEL2 WHERE NO=%s
            row = Table2.object.get(no=n)
            row.delete() #삭제

            return redirect('/board/t2_list')

@csrf_exempt
def t2_update(request):
        if request.method=='GET':
            n = request.GET.get('no',0)
            row = Table2.object.get(no=n)
            return render(request, 'board/t2_update.html', {'one':row})
        elif request.method=='POST':
                n=request.POST['no']
                obj = Table2.object.get(no=n)#obj객체 가져옴
                obj.name = request.POST['name']# 변수의 값
                obj.kor = request.POST['kor']
                obj.eng = request.POST['eng']
                obj.math = request.POST['math']
                obj.save() #저장하기 수행

                #UPDATE BOARD_TABLE2 SET
                # NAME=%s, KOR=%s, ENG = %s, MATH=%s WHERE=%s
                return redirect('/board/t2_list')
            

def t2_insert_all(request):
    if request.method=='GET':
        return render(request, 'board/t2_insert_all.html') #return render(request, 'board/t2_insert_all.html', {cnt:range(5)}) 랑 같음
    elif request.method=='POST':
        na=request.POST.getlist("name[]")
        ko=request.POST.getlist("kor[]")
        en=request.POST.getlist("eng[]")
        math=request.POST.getlist("math[]")
        objs=[]
        for i in range(0, len(na), 1):
            obj=Table2()
            obj.name = na[i]
            obj.kor = ko[i]
            obj.eng = en[i]
            obj.math = math[i]
            objs.append(obj)
        #일괄추가
        Table2.object.bulk_create(objs)    
        return redirect('/board/t2_insert')
@csrf_exempt
def t2_update_all(request):
    if request.method=='GET':
        n=request.session['no'] # 8, 5, 3
        print(n)
        rows = Table2.object.filter(no__in=n)
            #"SELECT * FROM BOARD_TABLE2 WHERE NO=8 OR NO =5 OR NO=3"
            #"SELECT * FROM BOARD_TABLE2 WHERE NO IN (8,5,3)"       
        return render(request, 'board/t2_update_all.html', {'list':rows})

    elif request.method=='POST':
        menu = request.POST['menu']
        
        if menu == '1':        
            no=request.POST.getlist('chk[]')
            request.session['no']=no
            return redirect('/board/t2_update_all')

        elif menu == '2':

            no=request.POST.getlist('no[]')
            name=request.POST.getlist('name[]')
            kor=request.POST.getlist('kor[]')
            eng=request.POST.getlist('eng[]')
            math=request.POST.getlist('math[]')
            objs=[]

            for i in range(0, len(no), 1):
                obj = Table2.object.get(no=no[i])
                obj.name = name[i]
                obj.kor = kor[i]
                obj.eng = eng[i]
                obj.math = math[i]
                objs.append(obj)
            Table2.object.bulk_update(objs,['name','kor','eng','math'])
            return redirect("/board/t2_list")

