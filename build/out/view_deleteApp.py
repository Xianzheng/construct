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
BASE_DIR = Path(__file__).resolve().parent
appName = str(BASE_DIR).split('\\')[-1]

def deleteFolderContent(folderPath):
    for root, dirs, files in os.walk(folderPath, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

def removePath(app_name):
    rootPath = os.getcwd()
    print('remove root path')

    app_name = urllib.parse.unquote(app_name)
    
    mainUrlPath = rootPath +'\\'+rootPath.split('\\')[-1]+'\\urls.py'
    
    originlst = []

    with open(mainUrlPath,'r',encoding='utf-8') as f:
        originlst = f.readlines()
    f.close()

    removePath ="path('{}/',include('{}.urls'))".format(app_name,app_name)

    afterRemovelst = [i for i in originlst if removePath not in i]

    afterRemoveString = ''.join(afterRemovelst)

    with open(mainUrlPath,'w',encoding='utf-8') as f:
        f.write(afterRemoveString)
    f.close()

   
    
def unistallApp(app_name):
    rootPath = os.getcwd()
    print('unistall app from settings')

    app_name = urllib.parse.unquote(app_name)
    
    mainSettingsPath = rootPath +'\\'+rootPath.split('\\')[-1]+'\\settings.py'
    
    originlst = []

    with open(mainSettingsPath,'r',encoding='utf-8') as f:
        originlst = f.readlines()
    f.close()

    removePath ="'{}.apps.{}Config'".format(app_name,app_name)

    afterRemovelst = [i for i in originlst if removePath not in i]

    # print(afterRemovelst)
    afterRemoveString = ''.join(afterRemovelst)

    with open(mainSettingsPath,'w',encoding='utf-8') as f:
        f.write(afterRemoveString)
    f.close()

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