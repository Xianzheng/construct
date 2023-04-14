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
import subprocess

BASE_DIR = Path(__file__).resolve().parent
appName = str(BASE_DIR).split('\\')[-1]



def streamlitShow_view(request):
    #根据表数据形成xls文件
    #将xls信息写入stramlit_show.py文件
    #streamlit run streamlit 文件
    oldPath = os.getcwd()
    print(oldPath)
    os.chdir(oldPath+'\\'+appName)
    # os.system("streamlit run streamlib_show.py")
    # cmd start不阻塞运行新的进程
    os.system('start streamlit run streamlit_show.py')
    
    os.chdir(oldPath)
    return HttpResponse('Hello')