from django.shortcuts import render, redirect
from django.http.response import HttpResponse
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

def screamlitShow_view(request):

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

    dic = {}
    for i in columns:
        dic[i] = []

    allTable = tableInstance.objects.all()
    for eachTable in allTable:
        for i in columns:
            dic[i].append(getattr(eachTable,i))

    df = pd.DataFrame(dic)

    DataFrame(df).to_excel('static.xls', sheet_name='Sheet1', index=False, header=True)
   
    # columnslst = tableInstance._meta.get_all_field_names()

    # print(columnslst)
    #运行streamlit
    """
    每个项目的streamlit_show.py文件得重新定制
    """
    os.system("start streamlit run streamlit_show.py")

    #变回之前的path
    os.chdir(oldPath)

    return redirect('/{}/table1/'.format(appName))
