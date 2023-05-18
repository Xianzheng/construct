from django.db import models
import datetime

class table1(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True,)
    设备 = models.CharField(max_length=20,default = '',verbose_name = '设备',blank = True)
    名称 = models.CharField(max_length=20,default = '',verbose_name = '名称',blank = True)
    规格型号 = models.CharField(max_length=20,default = '',verbose_name = '规格型号',blank = True)
    承修单 = models.CharField(max_length=20,default = '',verbose_name = '承修单',blank = True)
    维修费 = models.CharField(max_length=20,default = '',verbose_name = '维修费',blank = True)
    维修主要 = models.CharField(max_length=20,default = '',verbose_name = '维修主要',blank = True)
    原因分 = models.CharField(max_length=20,default = '',verbose_name = '原因分',blank = True)
    验收时 = models.CharField(max_length=20,default = '',verbose_name = '验收时',blank = True)
    保质期 = models.CharField(max_length=20,default = '',verbose_name = '保质期',blank = True)
    付款 = models.CharField(max_length=20,default = '',verbose_name = '付款',blank = True)
