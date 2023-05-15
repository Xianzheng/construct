from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from .tools import getmodelfield, loadData, getHeader
from .models import *
from .tools_visual import *
from .tools2 import *
from .tools_visual import *
from pathlib import Path
import os,json
import pandas as pd
from pandas import DataFrame
from .models import *
from .view_plugin_tools import *
from django import forms
from django.db.models import Q
BASE_DIR = Path(__file__).resolve().parent
searchInput= ''
appName = str(BASE_DIR).split('\\')[-1]
exclude = ['username','email','is_staff','last_login','password','last_name','date_joined','is_active','is_superuser']

BASE_DIR = Path(__file__).resolve().parent
rootFilePath = str(BASE_DIR).split('\\')[-1]

class search_Forms(forms.Form):
    searchContents= forms.CharField(label="关键字")
    
def searchInput_view(request):
    formName = 'search_Forms'
    form = globals()[formName]
    action = '/'+rootFilePath+'/searchOutput/'
    return render(request,'form.html',{'form':form,
    'title':'关键字查找','action':action,'tableName':'','goback':'','appName':'ABC'})
    
def searchOutput_view(request):
    form = search_Forms(request.POST)
    # data = form.cleaned_data
    # print(data)
    if form.is_valid():  # 进行数据校验
        # 校验成功
        data = form.cleaned_data  # 校验成功的值，会放在cleaned_data里。
        global searchInput
        searchInput = data
        # print(data)
        #提取database信息生成xls表
        #记录之前的path
        oldPath = os.getcwd()


        #改变到path至当前目录
        os.chdir(oldPath + '/'+appName)
        """
        提取数据库的所有数据生成 xls文件
        """

        #得到数据库里所有表名
        modelList = getModelList('./models.py')
        modelName = modelList[0]


        #得到表的实体
        tableInstance = globals()[modelName]
        columns = [f.get_attname() for f in tableInstance._meta.fields]
        columns = columns[1:]
        
        searchLst = []
        q1 = Q()
        q1.connector = 'OR'
        for i in columns:
            q1.children.append((i,data['searchContents']))
        

        objLst = tableInstance.objects.filter(q1)
        # print(objLst)
        
        os.chdir(oldPath)
        

        try:
            obj = objLst[0]
            #传入obj的字典格式obj.__dict__函数getheader得到表的第二项到最后一项
            cs = getmodelfield(rootFilePath, modelName,exclude)
            header = getHeader(obj.__dict__,start = 1, end = len(obj.__dict__) -1,cs = cs)
            header1 = getHeader(obj.__dict__,start = 2, end = (len(obj.__dict__)),cs = None)
            # print(header)
            #render style
            width = [100,150,100,150,100,150,100,150,100,150,100,150,100,150,100,150,100,150,100,150,100,150,100,150,100,150,100,150,100,150,100,150,]
            #render到那个template
            renderFile = './table/renderTable2.html' 
            #render header内容
            headerAndWidth = zip(header,width)
            #得到表的value
            #遍历所有表的所有信息填入进空的lst中
            totalData = loadData(objLst, header1)
            # print('line28',totalData)
            page_obj = getPaginationObject(request,totalData)

            #返回渲染template
            return render(request,renderFile,{'modelName':modelName,
                        'headerAndWidth':headerAndWidth,
                        'totalData':totalData,'status':0,
                        'tableName':'厂区表','tableId':0,
                        'goback':'/logout/',
                        'appName':'ABC','page_obj':page_obj})
        except:
            renderFile = './table/renderTable2.html'  
            return render(request,renderFile,{'modelName':modelName,
                        'headerAndWidth':'',
                        'totalData':'','status':0,
                        'tableName':'厂区表','tableId':0,
                        'goback':'/logout/','appName':'ABC'})

        # return HttpResponse(
        #     'ok'
        # )
        # return render(request, "add_emp.html", {"form": form})
    else:
        data = searchInput  # 校验成功的值，会放在cleaned_data里。
        
        print(data)
        #提取database信息生成xls表
        #记录之前的path
        oldPath = os.getcwd()


        #改变到path至当前目录
        os.chdir(oldPath + '/'+appName)
        """
        提取数据库的所有数据生成 xls文件
        """

        #得到数据库里所有表名
        modelList = getModelList('./models.py')
        modelName = modelList[0]


        #得到表的实体
        tableInstance = globals()[modelName]
        columns = [f.get_attname() for f in tableInstance._meta.fields]
        columns = columns[1:]
        
        searchLst = []
        q1 = Q()
        q1.connector = 'OR'
        for i in columns:
            q1.children.append((i,data['searchContents']))
        

        objLst = tableInstance.objects.filter(q1)
        # print(objLst)
        
        os.chdir(oldPath)
        

        try:
            obj = objLst[0]
            #传入obj的字典格式obj.__dict__函数getheader得到表的第二项到最后一项
            cs = getmodelfield(rootFilePath, modelName,exclude)
            header = getHeader(obj.__dict__,start = 1, end = len(obj.__dict__) -1,cs = cs)
            header1 = getHeader(obj.__dict__,start = 2, end = (len(obj.__dict__)),cs = None)
            # print(header)
            #render style
            width = [100,150,100,150,100,150,100,150,100,150,100,150,100,150,100,150,100,150,100,150,100,150,100,150,100,150,100,150,100,150,100,150,]
            #render到那个template
            renderFile = './table/renderTable1.html' 
            #render header内容
            headerAndWidth = zip(header,width)
            #得到表的value
            #遍历所有表的所有信息填入进空的lst中
            totalData = loadData(objLst, header1)
            # print('line28',totalData)
            page_obj = getPaginationObject(request,totalData)

            #返回渲染template
            return render(request,renderFile,{'modelName':modelName,
                        'headerAndWidth':headerAndWidth,
                        'totalData':totalData,'status':0,
                        'tableName':'厂区表','tableId':0,
                        'goback':'/logout/',
                        'appName':'ABC','page_obj':page_obj})
        except:
            renderFile = './table/renderTable1.html'  
            return render(request,renderFile,{'modelName':modelName,
                        'headerAndWidth':'',
                        'totalData':'','status':0,
                        'tableName':'厂区表','tableId':0,
                        'goback':'/logout/','appName':'ABC'})

        # return HttpResponse(
        #     'ok'
        # )
        # return render(request, "add_emp.html", {"form": form})
        
        
       
       

    