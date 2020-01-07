from django.db import models
#member/model.py
#python manage.py check
#python manage.py makemigrations member
#python manage.py migrate member
# Create your models here.


#1.MEMBER-TABLE2 회원을 20명 추가 하시오.
#EX)101 102 506 409
#URLS.PY
#EXAM_INSERT
#EXAM_UPDATE
#EXAM_DLELTE
#EXAM_SELECT


class table2(models.Model):
    object = models.Manager()#vs code 오류 제거용

    no     = models.AutoField(primary_key = True)#게시판 글 = 기본키 
    name   = models.CharField(max_length=30)#글 제목
    kor = models.IntegerField()
    eng = models.IntegerField()
    math = models.IntegerField()
    classroom = models.CharField(max_length=3)
    regdate = models.DateField(auto_now_add=True)