from django.urls import path ,include
from .views import *
from .views_visual import *
from .inputdata_view import *
urlpatterns = [
    path('table1/',table1_view),
    path('table2/<tableId>',table2_view),
    path('table3/<tableId>',table3_view),
    path('addSubTable/<tableId>/<tableModel>',addSubTable_view),
    path('updateRow/<modelName>/<rowId>/<tableId>',updateRow_view),
    path('deleteRow/<modelName>/<rowId>/<tableId>',deleteRow_view),
    path('visual1/',visual1_view),
    path('visual2/',visual2_view),
    path('add_data1/',add_data1_view),
    path('add_data2/',add_data2_view)
]
