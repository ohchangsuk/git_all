from django.db import models


#python manage.py check
#python manage.py makemigrations item
#python manage.py migrate item

# Create your models here.
class Item(models.Model):
    object=models.Manager()

    no     = models.AutoField(primary_key = True)#게시판 글 = 기본키 
    name   = models.CharField(max_length=30)
    price     = models.IntegerField()
    regdate = models.DateField(auto_now_add=True)