from .models import *
from django import forms
from .tools import *
import os,json
import pandas as pd

task_type_choices = (
        (0.5, 0.5),
        (1.0, 1.0),
        (2.0, 1.5),
        (2.0, 1.5),
    )

cost_type_choices = (
        ('水', '水'),
        ('电', '电'),
        ('气', '气'),
    )

oldPath = os.getcwd()
    # print(oldPath)
os.chdir(oldPath +'\\mystatic\\uploadFiles')


mainDf = pd.read_excel('basicdata.xls')
choiceLst = tuple(set(mainDf['使用部门']))
print(choiceLst)
os.chdir(oldPath)

choiceLst = (
    ('赤壁子公司','赤壁子公司'),
    ('武汉分公司','武汉分公司'),
)
    


class table1_Form(forms.ModelForm):

    class Meta:
        model = table1

        fields = "__all__"

        exclude = ['id','bind']
        

        widgets = {
                    '设备编号': forms.TextInput(attrs={'id':'使用时长_设备编号id','list':'使用时长_设备编号','onchange':"linkageAandB(this.value,'使用时长_设备名称id','设备编号','设备名称')"}),
                    '设备名称': forms.TextInput(attrs={'id':'使用时长_设备名称id','list':'使用时长_设备名称','onchange':"linkageAandB(this.value,'使用时长_设备编号id','设备名称','设备编号')"}),
                    '开机时间':  forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'}),
                    '使用部门': forms.Select(choices=choiceLst),
                    '关机时间':  forms.DateTimeInput(format=('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'}),
                    '操作时间': forms.Select(choices=task_type_choices),
                    '耗材使用': forms.Select(choices=cost_type_choices)
                }

        

        
            