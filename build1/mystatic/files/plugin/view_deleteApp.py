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

    #delete empty folder
    for root, dirs, files in os.walk(rootPath):
        if not os.listdir(root):
            os.rmdir(root)
    

    
    return HttpResponse(json.dumps({'fileList':'删除成功'}))

def getAppName_view(request):

    oldPath = os.getcwd()

    appNameList = os.listdir(oldPath)

    appNameList = [i for i in appNameList if i not in ['account', 'app', 'db.sqlite3', 'Log.txt', 'manage.py', 'mystatic']]
    
    return HttpResponse(json.dumps({'fileList':appNameList}))