from django.db import models
import datetime

class table1(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True,)
    title = models.CharField(max_length=20,default = '',verbose_name = '公司名',)

class table2(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True,)
    title = models.CharField(max_length=20,default = '',verbose_name = '气体',)
    bind = models.ForeignKey(table1,default=None,on_delete=models.CASCADE)

class table3(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True,)
    title = models.CharField(max_length=20,default = '',verbose_name = '比较',)
    bind = models.ForeignKey(table2,default=None,on_delete=models.CASCADE)

class table4(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True,)
    name= models.FloatField(default = 0.0,verbose_name = '消耗(吨)',)
    date= models.DateTimeField(verbose_name = '选择月份',)
    bind = models.ForeignKey(table3,default=None,on_delete=models.CASCADE)
