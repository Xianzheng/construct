# Generated by Django 3.2.18 on 2023-05-15 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('使用时长', '0008_alter_table1_关机时间'),
    ]

    operations = [
        migrations.AddField(
            model_name='table1',
            name='操作时间',
            field=models.FloatField(default=0.0, verbose_name='操作时间'),
        ),
    ]
