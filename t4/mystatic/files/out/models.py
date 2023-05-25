from django.db import models
import datetime

class table1(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True,)
    统计时间 = models.CharField(max_length=20,default = '',verbose_name = '统计时间',blank = True)
    水使用量吨 = models.CharField(max_length=20,default = '',verbose_name = '水使用量(吨)',blank = True)
    水花费元 = models.CharField(max_length=20,default = '',verbose_name = '水花费(元)',blank = True)
    电使用量千瓦时 = models.CharField(max_length=20,default = '',verbose_name = '电使用量(千瓦时)',blank = True)
    电花费元 = models.CharField(max_length=20,default = '',verbose_name = '电花费(元)',blank = True)
    二氧化碳使用量吨 = models.CharField(max_length=20,default = '',verbose_name = '二氧化碳使用量(吨)',blank = True)
    二氧化碳花费元 = models.CharField(max_length=20,default = '',verbose_name = '二氧化碳花费(元)',blank = True)
    液氧使用量吨 = models.CharField(max_length=20,default = '',verbose_name = '液氧使用量(吨)',blank = True)
    液氧花费元 = models.CharField(max_length=20,default = '',verbose_name = '液氧花费(元)',blank = True)
    氩气使用量吨 = models.CharField(max_length=20,default = '',verbose_name = '氩气使用量(吨)',blank = True)
    氩气花费元 = models.CharField(max_length=20,default = '',verbose_name = '氩气花费(元)',blank = True)
    丙烷使用量 = models.CharField(max_length=20,default = '',verbose_name = '丙烷使用量(kg)',blank = True)
    丙烷花费元 = models.CharField(max_length=20,default = '',verbose_name = '丙烷花费(元)',blank = True)
    混合气使用量瓶 = models.CharField(max_length=20,default = '',verbose_name = '混合气使用量(瓶)',blank = True)
    混合器花费元 = models.CharField(max_length=20,default = '',verbose_name = '混合器花费(元)',blank = True)
