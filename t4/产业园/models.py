from django.db import models
import datetime

class table1(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True,)
    年份 = models.CharField(max_length=20,default = '',verbose_name = '年份',blank = True)
    月份 = models.CharField(max_length=20,default = '',verbose_name = '月份',blank = True)
