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

def dealStatic_view(request):
    # userGroup = [i.name for i in request.user.groups.all()]
    # print(userGroup)
    return render(request,'dealStatic.html')