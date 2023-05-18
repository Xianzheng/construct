from .models import *
from django import forms

class table1_Form(forms.ModelForm):
    class Meta:
        model = table1

        fields = "__all__"

        exclude = ['id','bind']

        widgets = {
                    '设备编号': forms.TextInput(attrs={'id':'维修情况_设备编号id','list':'维修情况_设备编号','onchange':'linkageAandB(this.value,设备编号,设备名称)'}),
                    '设备名称': forms.TextInput(attrs={'id':'维修情况_设备名称id','list':'使用时长_设备名称','onchange':'func2(this.value)'}),
                    
                }


        
            