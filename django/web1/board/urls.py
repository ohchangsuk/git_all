#파일명 : board/urls.py

from django.urls import path
from . import views




#127.0.0.1:8080/member/abc => index 함수 동작
#view에 있는 index 함수를 실행 하라.
#urlpatterns는 url(주소/>>>>>이부분<<)에 있는 곳에 들어가서 views함수를 작동시켜라는 말임;
#127.0.0.1:8080/member/index
#127.0.0.1:8080/member/join
#127.0.0.1:8080/member/login
#크롬에 쳤을때 제일 처음에 urls에 들어와서 아래의 명령코드 들을 수행 그리고 views.py에 들어가서 함수 실행 

#

urlpatterns =[
    path('write', views.write, name='write'),
    path('list', views.list, name='list'),
    path('content', views.content, name='content'),
    path('edit', views.edit, name='edit'),
    path('delete', views.delete, name='delete'),
    path('dataframe', views.dataframe, name='dataframe'),
    path('t2_insert', views.t2_insert, name='t2_insert'),
    path('t2_list', views.t2_list, name='t2_list'),
    path('t2_delete', views.t2_delete, name='t2_delete'),
    path('t2_update', views.t2_update, name='t2_update'),
    path('t2_insert_all', views.t2_insert_all, name='t2_insert_all'),
    path('t2_update_all', views.t2_update_all, name='t2_update_all'),


]