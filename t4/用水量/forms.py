from .models import *
from django import forms

choiceYear = (
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        ('2026', '2026'),
        ('2027', '2027'),
        ('2028', '2028'),
        ('2029', '2029W'),
    )

choiceMonth = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    )

class table1_Form(forms.ModelForm):
    class Meta:
        model = table1

        fields = "__all__"

        exclude = ['id','bind']

        widgets = {
            '年份':  forms.Select(choices=choiceYear),
            '月份':  forms.Select(choices=choiceMonth),
            '水使用量吨':  forms.NumberInput(),

        }



        
            