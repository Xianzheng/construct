 
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
    department = '赤壁子公司'
    cond1 = mainDf['使用部门'] == department
    chibi = mainDf[cond1]
    group = chibi.groupby('设备名称')
    # department = '赤壁子公司'
    # lst = getDeviceList(mainDf,department)
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
    xlst = list(chibi.index)
    ylst = list(chibi.columns)[1:5]
    for x in xlst:
        lst = []
        for y in ylst:
            lst.append(chibi[y][x])
        # print(lst[1],lst[1],lst[2])
        
        fatherObj = globals()[faterTableName].objects.get(title=lst[2])
        globals()[clearTableName].objects.create(设备型号=str(lst[2]),设备编号=str(lst[0]),设备规格=str(lst[3]),制造商=str(lst[3]),bind=fatherObj)

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