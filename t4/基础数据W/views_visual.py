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
    root = os.getcwd()
    
    # return HttpResponse('hello')
    modelsList = getModelList('./{}/models.py'.format(appName))
    #创建一个字典收集结果，如果把字典放在for循环里每次都是空的字典
    result = {}
    xRes = []
    yRes = []
    pieResult = []
    for modelName in modelsList:
        #实体化model根据modelName具体到每一个model
        modelObj = globals()[modelName]
        value = modelObj.objects.all().count() 
        #得到每个model名字和有多少项内容
        # print(modelName)
        # print(modelObj.objects.all().count())
        result[modelName] = value
        # print(json.dumps(result))
        renderFile = './visual/renderVisual.html'
        #返回结果到网页
        xRes.append(modelName)
        yRes.append(value) 
        # {value:235, name:'视频广告'},
        pieResult.append({'value':value, 'name':modelName})
    result = {'xRes':xRes,'yRes':yRes}
    
    return render(request,renderFile,{'xRes':json.dumps(xRes),'yRes':json.dumps(yRes),'pieResult':json.dumps(pieResult),'appName':'app'})

@login_required(login_url="/acount/login/")
def visual2_view(request):
    #得到modes.py下的所有class
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
    
    

    '''
    # version 2
    for i in modelsList:
        dic = {}
        dic['obj'] = globals()[i].objects.all()
        dic['key'] = list(globals()[i].__dict__)[6]
        print(dic['key'])
        nodeLevelLst.append(globals()[i].objects.all())
    
    root = TreeNode('root',0,0)

    for i in nodeLevelLst[0]:
        node = TreeNode(i.title,i.id,1)
        root.add_child(node)

    for index in range(1,len(nodeLevelLst)):
        if index == 1:
            for i in NodeOfLevel(root,index):
                for j in nodeLevelLst[index]:
                    if i.id == j.bind.id:
                        # print(j.id,j.title)
                        node = TreeNode(j.title,j.id,index + 1)
                        i.add_child(node)
        else:
            for i in NodeOfLevel(root,index):
                for j in nodeLevelLst[index]:
                    if i.id == j.bind.id:
                        # print(j.id,j.title)
                        node = TreeNode(j.name,j.id,index + 1)
                        i.add_child(node)

    '''
    # return HttpResponse(modelsList)
    
    # firstLevel = globals()['table1'].objects.all()
    # secondLevel = globals()['table2'].objects.all()
    # thirdLevel = globals()['table3'].objects.all()
    # fourthLevel = globals()['table4'].objects.all()
    
    # lst = [secondLevel,thirdLevel,fourthLevel]
    
    # root = TreeNode('root',0,0)

    # for i in firstLevel:
    #     node = TreeNode(i.title,i.id,1)
    #     root.add_child(node)

    # # for i in NodeOfLevel(root,1):
    # #     print(i.name,i.id)

    # for i in NodeOfLevel(root,1):
    #     for j in secondLevel:
    #         if i.id == j.bind.id:
    #             # print(j.id,j.title)
    #             node = TreeNode(j.title,j.id,2)
    #             i.add_child(node)
    
    # for i in NodeOfLevel(root,2):
    #     for j in thirdLevel:
    #         if i.id == j.bind.id:
    #             # print(j.id,j.title)
    #             node = TreeNode(j.name,j.id,3)
    #             i.add_child(node)
    
    data = tree_to_dict(root)
    
    queue = []
    queue.append(root)

    # print(data)
    return render(request,'./visual/renderVisual2.html',{'info':json.dumps(data),'appName':'app'})