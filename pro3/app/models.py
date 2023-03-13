from django.db import models
import datetime

class table1(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True,)
    title = models.CharField(max_length=20,default = '',verbose_name = '主任')
    date= models.DateTimeField(verbose_name = '更改日期')

class table2(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True,)
    title = models.CharField(max_length=20,default = '',verbose_name = '副主任')
    date= models.DateTimeField(verbose_name = '更改日期')
    bind = models.ForeignKey(table1,default=None,on_delete=models.CASCADE)

class table3(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True,)
    name = models.CharField(max_length=20,default = '',verbose_name = '科员')
    old = models.CharField(max_length=20,default = '',verbose_name = '年限')
    date= models.DateTimeField(verbose_name = '更改日期')
    bind = models.ForeignKey(table2,default=None,on_delete=models.CASCADE)
