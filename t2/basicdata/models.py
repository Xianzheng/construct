from django.db import models
import datetime

class table1(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True,)
    设备编号 = models.CharField(max_length=20,default = '',verbose_name = '设备编号',blank = True)
    资产编号 = models.CharField(max_length=20,default = '',verbose_name = '资产编号',blank = True)
    设备名称 = models.CharField(max_length=20,default = '',verbose_name = '设备名称',blank = True)
    设备型号 = models.CharField(max_length=20,default = '',verbose_name = '设备型号',blank = True)
    设备规格 = models.CharField(max_length=20,default = '',verbose_name = '设备规格',blank = True)
    制造厂 = models.CharField(max_length=20,default = '',verbose_name = '制造厂',blank = True)
    使用部门 = models.CharField(max_length=20,default = '',verbose_name = '使用部门',blank = True)
