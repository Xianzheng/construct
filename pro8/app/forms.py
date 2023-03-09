from .models import *
from django import forms

class table1_Form(forms.ModelForm):
    class Meta:
        model = table1

        fields = "__all__"

        exclude = ['id','bind']


        
            
        widgets = {
                    'year': forms.widgets.DateInput(attrs={'type':'year'}),
                }
                
class table2_Form(forms.ModelForm):
    class Meta:
        model = table2

        fields = "__all__"

        exclude = ['id','bind']


        
            
        widgets = {
                    'year': forms.widgets.DateInput(attrs={'type':'year'}),
                }
                
class table3_Form(forms.ModelForm):
    class Meta:
        model = table3

        fields = "__all__"

        exclude = ['id','bind']


        
            
        widgets = {
                    'year': forms.widgets.DateInput(attrs={'type':'year'}),
                }
                