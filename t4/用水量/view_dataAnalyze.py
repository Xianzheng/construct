from django.shortcuts import render, redirect
from django.http.response import HttpResponse, FileResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .tools import *
from .tools_visual import *
from .tools2 import *
from pathlib import Path
import os,json
import pandas as pd
from pandas import DataFrame
BASE_DIR = Path(__file__).resolve().parent
appName = str(BASE_DIR).split('\\')[-1]

def monthDataAnalyze_view(request,data):
     #得到filename下模块名称表
    root = os.getcwd()
    print(type(data))
    data = data.replace('\'','').replace('[','').replace(']','')
    data = data.split(',')
    currentYear = int(data[0])
    currentMonth = int(data[1])
    # return HttpResponse('hello')
    modelsList = getModelList('./{}/models.py'.format(appName))
    department = getUrlParameter(request,'department=')
   
    #创建一个字典收集结果，如果把字典放在for循环里每次都是空的字典
    db = getThirdAppLib(request,appName).objects.filter(年份 = str(currentYear - 1) , 月份 = str(currentMonth),使用部门 = department)
    if db:
        for i in db:
            r = dict(list(i.__dict__.items())[4:-1])
            print(r)
        yRes = list(r.values())
    else:
        yRes = []

    # yRes是上一年的数据

    
    db1 = getThirdAppLib(request,appName).objects.filter(年份 = str(currentYear), 月份 = str(currentMonth),使用部门 = department)
    if db1:
        for i in db1:
            r1 = dict(list(i.__dict__.items())[4:-1])
        
        xRes1 = list(r1.keys())
        yRes1 = list(r1.values())

    else:
        yRes1 = []

    #yRes1是今年数据

    db2 = getThirdAppLib(request,appName).objects.filter(年份 = str(currentYear), 月份 = str(currentMonth - 1),使用部门 = department)
    if db2:
        for i in db2:
            r2 = dict(list(i.__dict__.items())[4:-1])
        
        yRes2 = list(r2.values())
    else:
        yRes2 = []

    #yRes2是上个月数据

    # return render(request,renderFile,{'xRes':json.dumps(xRes),'yRes':json.dumps(yRes),'pieResult':json.dumps(pieResult),'appName':'app'})
    return render(request,'./visual/renderVisual.html',{'xRes':json.dumps(xRes1),'yRes':json.dumps(yRes),
                                                        'yRes1':json.dumps(yRes1),'yRes2':json.dumps(yRes2),
                                                        'currentYear':json.dumps(currentYear),'currentMonth':json.dumps(currentMonth),
                                                        'appName':'app'})

def constantDataAnalyze_view(request):
    #显示路径，通过路径得到app name 和 deparment name
    url = request.get_full_path()
    #decode网页中文乱码
    url = urllib.parse.unquote(url)
    #通过'/'分离路径信息,lst[1]是projectName
    appName = url.split('/')[1]
    #通过'department='分离，lst[-1]是department name
    departmentName = url.split('department=')[-1]

    

    xRes = []
    yRes = []
    lib = getThirdAppLib(request,appName)
    obj = lib.objects.filter(使用部门=departmentName).order_by('年份','月份')
    for item in obj:
        xRes.append('{}年{}月'.format(item.年份,item.月份))
        yRes.append(item.水使用量吨)
    
    return render(request,'./visual/renderVisual1.html',{'xRes':json.dumps(xRes),'yRes':json.dumps(yRes)})

