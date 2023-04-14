from django.urls import path ,include
from .views import *
from .views_visual import *
from .view_deleteApp import *
from .view_plugin_tools import *
from .view_upload import *
urlpatterns = [
    path('table1/',table1_view),
    path('addSubTable/<tableId>/<tableModel>',addSubTable_view),
    path('updateRow/<modelName>/<rowId>/<tableId>',updateRow_view),
    path('deleteRow/<modelName>/<rowId>/<tableId>',deleteRow_view),
    path('visual1/',visual1_view),
    path('visual2/',visual2_view),
    path('deleteApp/',deleteApp_view),
    path('getAppName/',getAppName_view),
    path('upload/',upload_view),
    path('getUploadFiles/',getUploadFiles_view),
]
