from django.db import models
import datetime

class table1(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True,)
    设备编号 = models.CharField(max_length=20,default = '',verbose_name = '设备编号',blank = True)
    设备名称 = models.CharField(max_length=20,default = '',verbose_name = '设备名称',blank = True)
    开机时间= models.DateTimeField(verbose_name = '开机时间',blank = True)
    关机时间= models.DateTimeField(verbose_name = '关机时间',blank = True)
    操作时间= models.FloatField(verbose_name = '操作时间',blank = True)
    耗材使用 = models.CharField(max_length=20,default = '',verbose_name = '耗材使用',blank = True)
