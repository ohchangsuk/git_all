#member/ur1s.py

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
    path('index', views.index, name='index'),
    path('join', views.join, name='join'),
    path('login', views.login, name='login'),
    path('list1', views.list1, name='list1'),
    path('logout', views.logout, name='logout'),
    path('edit', views.edit, name='edit'),
    path('delete', views.delete, name='delete'),

    path('join1', views.join1, name='join1'),

    path('auth_join', views.auth_join, name='auth_join'),
    path('auth_index', views.auth_index, name='auth_index'),
    path('auth_login', views.auth_login, name='auth_login'),
    path('auth_logout', views.auth_logout, name='auth_logout'),
    path('auth_edit', views.auth_edit, name='auth_edit'),
    path('auth_pw', views.auth_pw, name='auth_pw'),

    path('exam_insert', views.exam_insert, name='exam_insert'),
    path('exam_update', views.exam_update, name='exam_update'),
    path('exam_delete', views.exam_delete, name='exam_delete'),
    path('exam_select', views.exam_select, name='exam_select'),

    path('js_index', views.js_index, name='js_index'),
    path('js_chart', views.js_chart, name='js_chart'),

    path('dataframe', views.dataframe, name='dataframe'),
    path('graph', views.graph, name='graph'),


#URLS.PY
#EXAM_INSERT
#EXAM_UPDATE
#EXAM_DLELTE
#EXAM_SELECT
]
