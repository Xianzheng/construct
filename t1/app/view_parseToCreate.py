# -*- coding:utf-8 _*-
import re
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .tools_visual import *
from .tools2 import *
from .tools import *
from pathlib import Path
import os,json,shutil,time
import urllib
from .view_plugin_tools import *
from django.core.management import call_command

BASE_DIR = Path(__file__).resolve().parent
appName = str(BASE_DIR).split('\\')[-1]
import pandas as pd

ses = 0

def parsingExcelToCreateApp_view(request):
    '''
    该方法
    '''
    parseCreatedApp = request.POST.get('parseCreatedApp')
    fileName = request.POST.get('fileName')
    oldPath = os.getcwd()
    
    os.chdir(os.getcwd()+'\\mystatic\\uploadFiles')
    mainDf = pd.read_excel(fileName)
    os.chdir(oldPath)
    #特殊字符
    specialChar = '([^\u4e00-\u9fa5\u0030-\u0039])'

    lst = [re.sub(specialChar,'',i) for i in mainDf.columns[1:]]
    # print(lst)

    #写入内容 #table1:id auto,设备编号 string,资产编号
    string = 'table1: id auto,'
    for i in mainDf.columns[1:]:
        string += '{} string vb-{},'.format(re.sub(specialChar,'',i),i)
    string = string[:-1]
    # print(string)

    #创建文件写入
    os.chdir(os.getcwd()+'\\mystatic\\uploadFiles')
    with open('drawModels.txt','w',encoding = 'utf-8') as f:
        f.write(string)
    f.close()

    #将drawModels.txt文件移到.\construct\t1\mystatic\files\draw
    # 当前路劲在
    # print('path is',os.getcwd())
    currentPath = os.getcwd()
    previouslst = currentPath.split('\\')[:-1]
    previousPath = '\\'.join(previouslst)
    # print(previousPath)
    shutil.copy(currentPath+'/drawModels.txt',previousPath+'/files/draw/drawModels.txt') 

    #根据输入的App名生成App
    targetPath = previousPath+'/files'    
    os.chdir(targetPath)
    # print(os.getcwd())
    os.system('python building.py '+parseCreatedApp)
    # print(parseCreatedApp)
    
   
    os.chdir(oldPath)



    
    return  HttpResponse(json.dumps({'fileList':'connect'}))

def getProcess_view(request):

    return HttpResponse(json.dumps({"process":ses}))

def autoAdd_data_view(request):
    # request.session["process"] = 20
    appName = request.POST.get('appName')
    fileName = request.POST.get('fileName')
    oldPath = os.getcwd()
    
    os.chdir(os.getcwd()+'\\mystatic\\uploadFiles')
    # print(os.getcwd())
    mainDf = pd.read_excel(fileName)
    os.chdir(oldPath)
    specialChar = '([^\u4e00-\u9fa5\u0030-\u0039])'
    
    import importlib
    # table1 = importlib.import_module('.models', package=appName)
    module=importlib.import_module(appName+".models")
    add = module.table1
    cleanLst = [re.sub(specialChar,'',i) for i in mainDf.columns[:]]
    #把mainDf 的columns 变成只保留汉字的
    mainDf.columns = cleanLst
    #得到objects.create(string)内容
    string1 = ''
    count = 0
    for i in cleanLst:
        string1 += i+'=str(lst[{}])'.format(count)+','
        count += 1
    string1 = string1[:-1]
    # print(string1)
    #添加进]
    # print(string1)
    # Model.objects.create（** data_dict）
    #globals()['add'].objects.create(设备编号=str(lst[0]),资产编号=str(lst[1]),设备名称=str(lst[2]),设备型号=str(lst[3]),设备规格=str(lst[4]),制造厂=str(lst[5]),出厂年月=str(lst[6]),使用部门=str(lst[7]),安装地点=str(lst[8]),立卡年月=str(lst[9]),启用年月=str(lst[10]),分类=str(lst[11]),财务分类=str(lst[12]),原值元=str(lst[13]),完好状态=str(lst[14]),当前管理状态=str(lst[15]),状态变动日期=str(lst[16]),使用年限年=str(lst[17]),供货商=str(lst[18]),出厂编号=str(lst[19]),单价元=str(lst[20]),设备属性=str(lst[21]),生产用途=str(lst[22]),责任人=str(lst[23]),备注=str(lst[24]))
    dic = {}
    for i in cleanLst[1:]:
        dic[i] = ''
    xlst = list(mainDf.index)
    ylst = list(mainDf.columns)[1:]
    # print(ylst)
    count = 1
    total = len(xlst)
    print(total)
    
    for x in xlst:
        lst = []
        for y in ylst:
            # lst.append(mainDf[y][x])
            
           
            
            # del request.session["process"]
            
            
            dic[y] = mainDf[y][x]
            # print(count)
        # add.objects.create(globals()[string1])
        add.objects.create(**dic)
        count += 1
        global ses 
        ses =  int(count/total * 100)
        # request.session.flush()
        # request.session['process'] = int(count/total * 100)
        # response.set_signed_cookie(key,value,salt='加密盐',...)
        print(ses)
        # print(request.session.get('process'))

        # print('percent:',int(count/total * 100))

    
   
    
    return HttpResponse(json.dumps({'msg':'success'}))