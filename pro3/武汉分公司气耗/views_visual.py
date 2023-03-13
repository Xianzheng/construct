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

@login_required(login_url="/acount/login/")
def visual1_view(request):
    #得到filename下模块名称表
    root = makeAtree()
    name = 'LCO2'
    pick = '计划'
    node = findNodeByName(root,name)
    ylst = []
    pieResult = []
    count = 1;
    
    for i in node.children[0].children:
        
        ylst.append(i.name)
        pieResult.append({'value':i.name, 'name':str(count)+'月'})
        count += 1

    xlst = [str(i) + '月' for i in range(1,len(ylst) + 1)]

    dataNameLst = []
    for i in NodeOfLevel(root,2):
        dataNameLst.append(i.name)

    
    return render(request,'./visual/renderVisual.html',{'xRes':json.dumps(xlst),'yRes':json.dumps(ylst),'pieResult':json.dumps(pieResult),
                                                        'namelst':dataNameLst,'name':name})

@login_required(login_url="/acount/login/")
def visual2_view(request):
    #得到modes.py下的所有class
    
    root = makeAtree()

    data = tree_to_dict(root)
    
    queue = []
    queue.append(root)

    # print(data)
    return render(request,'./visual/renderVisual2.html',{'info':json.dumps(data),'appName':'app'})

def makeAtree():

    modelsList = getModelList('./{}/models.py'.format(appName))
    # print(modelsList)
    
    nodeLevelLst = []

    for i in modelsList:
        dic = {}
        nodeLevelLst.append(globals()[i].objects.all())
    
    root = TreeNode('root',0,0)

    for i in nodeLevelLst[0]:
        key = list(i.__dict__)[2]
        node = TreeNode(getattr(i,key),i.id,1)
        root.add_child(node)

    for index in range(1,len(nodeLevelLst)):
            
            for i in NodeOfLevel(root,index):
                for j in nodeLevelLst[index]:
                    if i.id == j.bind.id:
                        key = list(j.__dict__)[2]
                        node = TreeNode(getattr(j,key),j.id,index + 1)
                        i.add_child(node)

    return root