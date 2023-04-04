from django.db import models
import datetime

class table1(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True,)
    设备编号 = models.CharField(max_length=20,default = '',)
