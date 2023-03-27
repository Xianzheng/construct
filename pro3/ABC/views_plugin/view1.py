from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from pathlib import Path
import os,django
from ..models import *

def code1_view(request):
    
    obj = globals()['table1']
    obj.objects.create(title="随便")
    return redirect('/ABC/table1')

def code2_view(request):

    parentClass = globals()['table1']
    parentObj = parentClass.objects.get(title="随便")
    childClass = globals()['table2']
    childClass.objects.create(title = 1, bind=parentObj)
    childClass.objects.create(title = 2, bind=parentObj)
    childClass.objects.create(title = 3, bind=parentObj)