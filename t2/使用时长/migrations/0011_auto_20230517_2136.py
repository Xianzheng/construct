# Generated by Django 3.2.18 on 2023-05-18 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('使用时长', '0010_auto_20230517_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table1',
            name='关机时间',
            field=models.DateTimeField(blank=True, verbose_name='关机时间'),
        ),
        migrations.AlterField(
            model_name='table1',
            name='开机时间',
            field=models.DateTimeField(blank=True, verbose_name='开机时间'),
        ),
        migrations.AlterField(
            model_name='table1',
            name='操作时间',
            field=models.FloatField(blank=True, verbose_name='操作时间'),
        ),
    ]
