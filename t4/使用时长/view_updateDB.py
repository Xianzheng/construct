from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from .tools import getmodelfield, loadData, getHeader
from .models import *
from .forms import *
from pathlib import Path
from django.http.response import HttpResponse
from django.core.management import call_command
from .view_plugin_tools import *
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings")
django.setup()
import urllib
import sys

def updateDB_view(request):
    import json
    print(request.get_full_path())
    path = request.get_full_path()
    appName = path.split('/')[1]
    appName = urllib.parse.unquote(appName)
    print(appName)
    call_command("makemigrations")
    call_command("migrate")
    return redirect('/{}/table1/'.format(appName))