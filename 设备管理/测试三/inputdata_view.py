 
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from .tools import getmodelfield, loadData, getHeader,getCurrentFolderRootName
from .models import *
from .tools_visual import *
from .forms import *
from pathlib import Path
import os,django
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
appName = str(BASE_DIR).split('\\')[-1]

def getDeviceList(mainDf,department):
    cond1 = mainDf['使用部门'] == department
    chibi = mainDf[cond1]
    chibiShebei = chibi['设备名称']
    s = set()
    for i in chibiShebei:
        if i in s:
            pass
        else:
            s.add(i)
    return list(s)




def add_data1_view(request):

    olderPath = os.getcwd()
    folderRootName = getCurrentFolderRootName(request.path)
    newpath = str(os.getcwd())+'/'+ folderRootName
    os.chdir(newpath)
    print(os.getcwd())
    mainDf = pd.read_excel('./设备台帐信息2022.11.08.xls')
    os.chdir(olderPath)
    department = '赤壁子公司'
    lst = getDeviceList(mainDf,department)
    tableName = ''
    fullPath = request.get_full_path()
    if '?' in fullPath:
        tableName = fullPath.split('=')[-1]
    
    #
    clearTableName = tableName[:-1]
    modelsList = getModelList('./{}/models.py'.format(appName))

    currentTableIndex = modelsList.index(clearTableName)
    previousTableIndex = currentTableIndex - 1

    faterTableName = modelsList[previousTableIndex]

    fatherObj = globals()[faterTableName].objects.get(title=department)
    # print(faterTableName)
    # print(modelsList)
    for i in lst:

        globals()[clearTableName].objects.create(title=i,bind=fatherObj)
        
    
    return HttpResponse('happy')



def add_data2_view(request):

    olderPath = os.getcwd()
    folderRootName = getCurrentFolderRootName(request.path)
    newpath = str(os.getcwd())+'/'+ folderRootName
    os.chdir(newpath)
    print(os.getcwd())
    mainDf = pd.read_excel('./设备台帐信息2022.11.08.xls')
    os.chdir(olderPath)
    
    xlst = list(mainDf.index)
    ylst = list(mainDf.columns)[1:]
    for x in xlst:
        lst = []
        for y in ylst:
            lst.append(mainDf[y][x])
        # print(lst[1],lst[1],lst[2])
        
        
        globals()['table1'].objects.create(设备编号=str(lst[0]),资产编号=str(lst[1]),设备名称=str(lst[2]),设备型号=str(lst[3]),设备规格=str(lst[4]),制造厂=str(lst[5]),出厂年月=str(lst[6]),使用部门=str(lst[7]),安装地点=str(lst[8]),立卡年月=str(lst[9]),启用年月=str(lst[10]),ABC分类=str(lst[11]),财务分类=str(lst[12]),原值元=str(lst[13]),完好状态=str(lst[14]),当前管理状态=str(lst[15]),状态变动日期=str(lst[16]),使用年限年=str(lst[17]),供货商=str(lst[18]),出厂编号=str(lst[19]),单价元=str(lst[20]),设备属性=str(lst[21]),生产用途=str(lst[22]),责任人=str(lst[23]),备注=str(lst[24]))

    # for i, j  in group:
    #     fatherObj = globals()[faterTableName].objects.get(title=i)
    #     xlst = list(j.index)
    #     ylst = list(j.columns)[1:5]
    #     for x in xlst:
    #         lst = []
    #         for y in ylst:
    #             lst.append(j[y][x])
    

            
    # fatherObj = globals()[faterTableName].objects.get(title=department)
    # # print(faterTableName)
    # # print(modelsList)
    # for i in lst:

    #     globals()[clearTableName].objects.create(title=i,bind=fatherObj)


        
    
    return HttpResponse('happy1')