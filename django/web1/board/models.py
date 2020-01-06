from django.db import models

# Create your models here.


class table1(models.Model):
    object = models.Manager()#vs code 오류 제거용

    no     = models.AutoField(primary_key = True)#게시판 글 = 기본키 
    title   = models.CharField(max_length=200)#글 제목
    content = models.TextField()#내용은 길이를 모르니깐 텍스트로
    writer  = models.CharField(max_length=50)
    hit     = models.IntegerField()
    regdate = models.DateField(auto_now_add=True)
    img     = models.BinaryField(null=True)


class Table2(models.Model):
    object = models.Manager() # vs오류 제거용

    no     = models.AutoField(primary_key = True)#게시판 글 = 기본키 
    name   = models.CharField(max_length=200)#글 제목
    kor = models.IntegerField()
    eng = models.IntegerField()
    mat = models.IntegerField()
    regdate = models.DateField(auto_now_add=True)
