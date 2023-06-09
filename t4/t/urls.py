from django.urls import path ,include
from .views import *
from .views_visual import *
from .view_dataAnalyze import *
from .view_export import *
from .view_plugin_tools import *
from .view_screamlitShow import *
from .view_search import *
urlpatterns = [
    path('table1/',table1_view),
    path('addSubTable/<tableId>/<tableModel>',addSubTable_view),
    path('updateRow/<modelName>/<rowId>/<tableId>',updateRow_view),
    path('deleteRow/<modelName>/<rowId>/<tableId>',deleteRow_view),
    path('visual1/',visual1_view),
    path('visual2/',visual2_view),
    path('monthDataAnalyze/',monthDataAnalyze_view),
    path('export/',export_view),
    path('screamlitShow/',screamlitShow_view),
    path('searchInput/',searchInput_view),
    path('searchOutput/',searchOutput_view),
]
