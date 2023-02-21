from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .tools_visual import *
from .tools2 import *
import os,json



@login_required(login_url="/acount/login/")
def visual1_view(request):
    #得到filename下模块名称表
    root = os.getcwd()
    
    # return HttpResponse('hello')
    modelsList = getModelList('./app/models.py')
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
    
    return render(request,renderFile,{'xRes':json.dumps(xRes),'yRes':json.dumps(yRes),'pieResult':json.dumps(pieResult)})

@login_required(login_url="/acount/login/")
def visual2_view(request):
    modelsList = getModelList('./app/models.py')
    
    firstLevel = globals()['table1'].objects.all()
    secondLevel = globals()['table2'].objects.all()
    thirdLevel = globals()['table3'].objects.all()
    fourthLevel = globals()['table4'].objects.all()
    
    lst = [secondLevel,thirdLevel,fourthLevel]
    
    root = TreeNode('root',0,0)

    for i in firstLevel:
        node = TreeNode(i.title,i.id,1)
        root.add_child(node)

    for i in NodeOfLevel(root,1):
        print(i.name,i.id)

    for i in NodeOfLevel(root,1):
        for j in secondLevel:
            if i.id == j.bind.id:
                # print(j.id,j.title)
                node = TreeNode(j.title,j.id,2)
                i.add_child(node)
    
    for i in NodeOfLevel(root,2):
        for j in thirdLevel:
            if i.id == j.bind.id:
                # print(j.id,j.title)
                node = TreeNode(j.name,j.id,3)
                i.add_child(node)
    
    

    data = tree_to_dict(root)
    

    
    queue = []
    queue.append(root)

    
        
    # print(data)
    return render(request,'./visual/renderVisual2.html',{'info':json.dumps(data)})