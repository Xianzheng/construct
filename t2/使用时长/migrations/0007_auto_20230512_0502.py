# Generated by Django 3.2.18 on 2023-05-12 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('使用时长', '0006_rename_运行时间_table1_开机时间'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table1',
            name='使用时间',
        ),
        migrations.AddField(
            model_name='table1',
            name='关机时间',
            field=models.FloatField(default=0.0, verbose_name='关机时间'),
        ),
        migrations.AlterField(
            model_name='table1',
            name='开机时间',
            field=models.DateTimeField(default=0.0, verbose_name='开机时间'),
        ),
    ]
