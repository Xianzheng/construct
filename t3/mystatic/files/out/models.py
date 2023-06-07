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
    出厂年月 = models.CharField(max_length=20,default = '',verbose_name = '出厂年月',blank = True)
    使用部门 = models.CharField(max_length=20,default = '',verbose_name = '使用部门',blank = True)
    安装地点 = models.CharField(max_length=20,default = '',verbose_name = '安装地点',blank = True)
    立卡年月 = models.CharField(max_length=20,default = '',verbose_name = '立卡年月',blank = True)
    启用年月 = models.CharField(max_length=20,default = '',verbose_name = '启用年月',blank = True)
    分类 = models.CharField(max_length=20,default = '',verbose_name = 'ABC分类',blank = True)
    财务分类 = models.CharField(max_length=20,default = '',verbose_name = '财务分类',blank = True)
    原值元 = models.CharField(max_length=20,default = '',verbose_name = '原值(元)',blank = True)
    完好状态 = models.CharField(max_length=20,default = '',verbose_name = '完好状态',blank = True)
    当前管理状态 = models.CharField(max_length=20,default = '',verbose_name = '当前管理状态',blank = True)
    状态变动日期 = models.CharField(max_length=20,default = '',verbose_name = '状态变动日期',blank = True)
    使用年限年 = models.CharField(max_length=20,default = '',verbose_name = '使用年限(年)',blank = True)
    供货商 = models.CharField(max_length=20,default = '',verbose_name = '供货商',blank = True)
    出厂编号 = models.CharField(max_length=20,default = '',verbose_name = '出厂编号',blank = True)
    单价元 = models.CharField(max_length=20,default = '',verbose_name = '单价(元)',blank = True)
    设备属性 = models.CharField(max_length=20,default = '',verbose_name = '设备属性',blank = True)
    生产用途 = models.CharField(max_length=20,default = '',verbose_name = '生产用途',blank = True)
    责任人 = models.CharField(max_length=20,default = '',verbose_name = '责任人',blank = True)
    备注 = models.CharField(max_length=20,default = '',verbose_name = '备注',blank = True)