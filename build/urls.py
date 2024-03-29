from django.urls import path ,include
from .views import *
from .views_visual import *
from .view_upload import *
from .view_deleteApp import *
urlpatterns = [
    path('table1/',table1_view),
    path('table2/<tableId>',table2_view),
    path('table3/<tableId>',table3_view),
    path('addSubTable/<tableId>/<tableModel>',addSubTable_view),
    path('updateRow/<modelName>/<rowId>/<tableId>',updateRow_view),
    path('deleteRow/<modelName>/<rowId>/<tableId>',deleteRow_view),
    path('addApp/',addApp_view),
    path('updateDB/',updateDB_view),
    path('getApp/',getApp_view),
    path('visual1/',visual1_view),
    path('visual2/',visual2_view),
    path('upload/',upload_view),
    path('getUploadFiles/',getUploadFiles_view),
    path('getAppName/',getAppName_view),
    path('deleteApp/',deleteApp_view),
]
