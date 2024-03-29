# Generated by Django 3.2.18 on 2023-04-28 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('设备编号', models.CharField(blank=True, default='', max_length=20, verbose_name='设备编号')),
                ('资产编号', models.CharField(blank=True, default='', max_length=20, verbose_name='资产编号')),
                ('设备名称', models.CharField(blank=True, default='', max_length=20, verbose_name='设备名称')),
                ('设备型号', models.CharField(blank=True, default='', max_length=20, verbose_name='设备型号')),
                ('设备规格', models.CharField(blank=True, default='', max_length=20, verbose_name='设备规格')),
                ('制造厂', models.CharField(blank=True, default='', max_length=20, verbose_name='制造厂')),
                ('出厂年月', models.CharField(blank=True, default='', max_length=20, verbose_name='出厂年月')),
                ('使用部门', models.CharField(blank=True, default='', max_length=20, verbose_name='使用部门')),
                ('安装地点', models.CharField(blank=True, default='', max_length=20, verbose_name='安装地点')),
                ('立卡年月', models.CharField(blank=True, default='', max_length=20, verbose_name='立卡年月')),
                ('启用年月', models.CharField(blank=True, default='', max_length=20, verbose_name='启用年月')),
                ('分类', models.CharField(blank=True, default='', max_length=20, verbose_name='ABC分类')),
                ('财务分类', models.CharField(blank=True, default='', max_length=20, verbose_name='财务分类')),
                ('原值元', models.CharField(blank=True, default='', max_length=20, verbose_name='原值(元)')),
                ('完好状态', models.CharField(blank=True, default='', max_length=20, verbose_name='完好状态')),
                ('当前管理状态', models.CharField(blank=True, default='', max_length=20, verbose_name='当前管理状态')),
                ('状态变动日期', models.CharField(blank=True, default='', max_length=20, verbose_name='状态变动日期')),
                ('使用年限年', models.CharField(blank=True, default='', max_length=20, verbose_name='使用年限(年)')),
                ('供货商', models.CharField(blank=True, default='', max_length=20, verbose_name='供货商')),
                ('出厂编号', models.CharField(blank=True, default='', max_length=20, verbose_name='出厂编号')),
                ('单价元', models.CharField(blank=True, default='', max_length=20, verbose_name='单价(元)')),
                ('设备属性', models.CharField(blank=True, default='', max_length=20, verbose_name='设备属性')),
                ('生产用途', models.CharField(blank=True, default='', max_length=20, verbose_name='生产用途')),
                ('责任人', models.CharField(blank=True, default='', max_length=20, verbose_name='责任人')),
                ('备注', models.CharField(blank=True, default='', max_length=20, verbose_name='备注')),
            ],
        ),
    ]
