from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .tools_visual import *
from .tools2 import *
from pathlib import Path
import os,json
BASE_DIR = Path(__file__).resolve().parent
appName = str(BASE_DIR).split('\\')[-1]

def upload_view(request):
    if request.method == 'POST':
        
        import json
        appName = request.POST.get('name')
        obj = request.FILES.get('key', '1')
        print(obj)
        print(appName)
        print(os.getcwd())
        oldPath = os.getcwd()
        os.chdir(os.getcwd()+'\\mystatic\\uploadFiles')
        f = open(obj.name,'wb')
        for chunk in obj.chunks():
            f.write(chunk)
        f.close()
        os.chdir(oldPath)

        
        # creat_app = appName
        # root = BASE_DIR
        # tem = str(root).split('\\')[:-1]
        # temp = '//'.join(tem)
        
        # os.chdir(temp+ '\\mystatic\\files')
        # # print(root)
        # print(os.getcwd())
        # os.system('python building.py '+creat_app)
        # os.chdir(root)
        
        # call_command("makemigrations")
        # call_command("migrate")
        return HttpResponse(json.dumps({'msg':'successful create'}))
    else:
    
        return render(request,'upload.html',{'appName':'app'})
    

def getUploadFiles_view(request):
    oldPath = os.getcwd()

    os.chdir(os.getcwd()+'\\mystatic\\uploadFiles')
    currentPath = os.getcwd()
    
    lst = os.listdir(currentPath) 

    lst = [i for i in lst if '.xls' in i or 'xlsx' in i]

    os.chdir(oldPath)

    return  HttpResponse(json.dumps({'fileList':lst}))