from django.urls import path ,include
from .views import *
from .views_visual import *
from .views_plugin import view1
urlpatterns = [
    path('table1/',table1_view),
    path('table2/<tableId>',table2_view),
    path('table3/<tableId>',table3_view),
    path('table4/<tableId>',table4_view),
    path('addSubTable/<tableId>/<tableModel>',addSubTable_view),
    path('updateRow/<modelName>/<rowId>/<tableId>',updateRow_view),
    path('deleteRow/<modelName>/<rowId>/<tableId>',deleteRow_view),
    path('visual1/',visual1_view),
    path('visual2/',visual2_view),
    path('code1/',view1.code1_view),
    path('code2/',view1.code2_view),
]
