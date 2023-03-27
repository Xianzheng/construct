from django.db import models
import datetime

class table1(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True,)
    title = models.CharField(max_length=20,default = '',verbose_name = '使用部门')

class table2(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True,)
    title = models.CharField(max_length=20,default = '',verbose_name = '设备名称')

class table3(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True,)
    设备编号 = models.CharField(max_length=20,default = '',)
    设备型号 = models.CharField(max_length=20,default = '',)
    设备规格 = models.CharField(max_length=20,default = '',)
    制造商 = models.CharField(max_length=20,default = '',)
