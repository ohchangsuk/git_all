from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt    


#insert1
from.models import Item
# Create your views here.

#select1
from . serializers import ItemSerializer
from rest_framework.renderers import JSONRenderer
import json


#127.0.0.1:8000/api/select1?key=abc
#{'id':'a'} > 물품 1개 

def select1(request):
    key=request.GET.get("key",'') 
    no=request.GET.get("no",'1')
    num=int(request.GET.get('num','1'))
    search=request.GET.get("search",'1')
    
    #db에서 확인

    if key=='abc':
        obj = Item.object.filter(name__contains='search')[0:int(num)]

        serializer = ItemSerializer(obj)

        data=JSONRenderer().render(serializer.data)
        return HttpResponse(data)        
    else:
        data=json.dumps({'ret':'key error'})
        return HttpResponse(data)

def select2(request):
    obj = Item.object.all()
    Serializer = Item
    Serializer(obj, many=True)

    data=JSONRenderer().render(serializer.data)
    return HttpResponse(data)


@csrf_exempt
def insert1 (request):
    for i in range(1,31,1):
        obj=Item()
        obj.name = '컴퓨터'+str(i)
        obj.price = 6000+i
        obj.save()
    return HttpResponse('insert1')

