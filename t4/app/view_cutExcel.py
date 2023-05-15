from django.shortcuts import render, redirect
from django.http.response import HttpResponse, FileResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .tools_visual import *
from .tools2 import *
from pathlib import Path
import os,json
import pandas as pd
from pandas import DataFrame
BASE_DIR = Path(__file__).resolve().parent
appName = str(BASE_DIR).split('\\')[-1]



def getChoice_view(request):
    #切换到上传文件目录
    oldPath = os.getcwd()
    # print(oldPath)
    os.chdir(oldPath +'\\mystatic\\uploadFiles')

    fileName = request.POST.get('fileName')
    mainDf = pd.read_excel(fileName)

    
    choiceLst = list(set(mainDf['使用部门']))

    print(choiceLst)
    # for index,content in enumerate(mainDf.columns[1:]):
    #     choiceLst.append(content)

    #切回主目录
    os.chdir(oldPath)
    return HttpResponse(json.dumps(choiceLst))

def cutFile_view(request):
    #切换到上传文件目录
    oldPath = os.getcwd()
    os.chdir(oldPath +'\\mystatic\\uploadFiles')
    #得到前端选择的文件名
    fileName = request.POST.get('fileName')
    mainDf = pd.read_excel(fileName)

    #前端传进的array后端也会变成一个字符串
    choose = request.POST.get('choose')
    chooselst = choose.split(',')
    print(chooselst)

    # queryString = ''
    # for i , j in enumerate(chooselst):
    #     if i != len(chooselst) - 1:
    #         queryString += '使用部门 == '+ j + ' | '
    #     else:
    #         queryString += '使用部门 == '+ j
    
    # print(queryString)
    # df = mainDf[mainDf['使用部门'] == '赤壁子公司']
    # df = mainDf.query(queryString)
    df = ''
    for i in chooselst:
        df = mainDf[mainDf['使用部门'] == i]
        

    DataFrame(df).to_excel('{}.xls'.format(choose), sheet_name='Sheet1', index=False, header=True)

    file = open('{}.xls'.format(choose), 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="excel.xls"'
    #变回之前的path
    os.chdir(oldPath)
    # return response
    return HttpResponse(json.dumps({"msg":"success"}))
