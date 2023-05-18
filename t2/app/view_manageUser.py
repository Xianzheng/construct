# -*- coding:utf-8 _*-

from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .tools_visual import *
from .tools2 import *
from pathlib import Path
import os,json
import urllib
from .view_plugin_tools import *
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

BASE_DIR = Path(__file__).resolve().parent
appName = str(BASE_DIR).split('\\')[-1]

def manageUser_view(request):
    return render(request,'manageUser.html')

def addUser_view(request):
    status = 0
    if request.method == 'POST':
        status = 1
        username = request.POST.get('username')
        password = request.POST.get('password')
        groupPermission = request.POST.get('groupPermission')
        # print('username is',username,'password',password,groupPermission)
        grouplst = Group.objects.all()
        #第一次创建组1，2，3
        if not grouplst:
            Group.objects.get_or_create(name = '1')
            Group.objects.get_or_create(name = '2')
            Group.objects.get_or_create(name = '3')
        # 判断该用户名是否存在
        lst = User.objects.filter(username = username)

        if lst:
            return HttpResponse(json.dumps({'msg':'existed'}))
        else:
            user=User.objects.create_user(username,"{}@reboot.com".format(username),password)
            new_group = Group.objects.get(name = groupPermission)
            user.groups.add(new_group)
            user.save()
            return HttpResponse(json.dumps({'msg':'success'}))
        
    return HttpResponse(json.dumps({'msg':status}))

def getUserList_view(request):
    userlst = User.objects.all()

    lst = [i.username for i in userlst]

    return HttpResponse(json.dumps({'fileList':lst}))

def deleteUser_view(request):
    username = request.POST.get('username')
    obj = User.objects.get(username=username)
    obj.delete()
    return HttpResponse(json.dumps({'mag':'success'}))