from flask import Flask, render_template, request, redirect

import cx_Oracle as oci #conda install cx_oracle

#아이디 /암호@서버주소:포트번호/SID
conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding='utf-8')
cursor=conn.cursor()

print(conn)


app = Flask(__name__)

@app.route('/')
def index():
    sql = "SELECT * FROM MEMBER"
    cursor.execute(sql)
    data = cursor.fetchall()

    return render_template('list.html',list=data)

@app.route('/join', methods=['GET'])
def join():
    return render_template('join.html')# join.html을 화면에 뿌려라 

@app.route('/join',methods=['POST'])
def join_post():
    #db에 값을 넣고
    a = request.form['id']
    b = request.form['pw']
    c = request.form['name']
    d = request.form['age']
    #print('{}:{}:{}:{}'.format(a,b,c,d))
    sql = 'INSERT INTO MEMBER VALUES(:id, :pw, :na, :ag, SYSDATE)'#sql문 외우면 좋음
    
    cursor.execute(sql, id=a, pw=b, na=c, ag=d)
    conn.commit()
    #오라클 db접속
    #추가하는 sql문 작성 > INSERT, SELECT, UPDATE, DELETE
    #SQL문 작성



    return redirect('/')#127.0.0.1:5000/ 주소이동,하는 명령어
    #127.0.0.1/ 크롬에서 입력한것 처럼 동작

@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')# join.html을 화면에 뿌려라 

@app.route('/login',methods=['POST'])
def login_post():
    #db에 값을 넣고
    print('login-post')


    return redirect('/')#127.0.0.1:5000/ 주소이동,하는 명령어
    #127.0.0.1/ 크롬에서 입력한것 처럼 동작


if __name__ =='__main__':
    app.run(debug=True) # 개발할때 모드 임;?