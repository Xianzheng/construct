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
BASE_DIR = Path(__file__).resolve().parent
appName = str(BASE_DIR).split('\\')[-1]



def deleteApp_view(request):

    rootPath = os.getcwd()
    
    appName = request.get_full_path().split('=')[1]
    
    appName = appName.split('/')[0]

    '''
        remove path from main Path
    '''
    removePath(appName)

    '''
        unInstallApp from setting
    '''
    unistallApp(appName)
    '''
        delete all files
    '''
    print('delete All Files')
    appName = urllib.parse.unquote(appName)

    folderPath = rootPath +'\\'+appName

    # print(folderPath)

    deleteFolderContent(folderPath)

    lst = [i for i in os.listdir(rootPath) if '.' not in i]

    #delete empty folder
    for item in lst:
        if not os.listdir(item):
            os.rmdir(item)
    # os.rmdir(rootPath)
    # print('os list is',os.listdir(rootPath))
    

    
    return HttpResponse(json.dumps({'fileList':'删除成功'}))

def getAppName_view(request):

    oldPath = os.getcwd()

    appNameList = os.listdir(oldPath)

    appNameList = [i for i in appNameList if i not in ['account', 'app', 'db.sqlite3', 'Log.txt', 'manage.py', 'mystatic']]
    
    return HttpResponse(json.dumps({'fileList':appNameList}))