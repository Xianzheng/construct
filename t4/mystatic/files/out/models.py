from django.db import models
import datetime

class table1(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True,)
    年份 = models.CharField(max_length=20,default = '',verbose_name = '年份',blank = True)
    月份 = models.CharField(max_length=20,default = '',verbose_name = '月份',blank = True)
    电使用量千瓦时 = models.CharField(max_length=20,default = '',verbose_name = '电使用量(千瓦时)',blank = True)
    使用部门 = models.CharField(max_length=20,default = '',verbose_name = '使用部门',blank = True)



    def __str__(self) -> str:
        return '{}{}年{}月用水量'.format(self.使用部门,self.年份,self.月份)

class tempModel(models.Model):
    def __str__(self) -> str:
        return 
    pass
        
