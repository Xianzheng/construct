# Generated by Django 3.2.18 on 2023-05-24 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('武汉厂区', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table1',
            name='统计时间',
            field=models.FloatField(blank=True, default=0.0, verbose_name='统计时间'),
        ),
    ]
