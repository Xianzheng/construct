# Generated by Django 3.2.18 on 2023-06-08 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('用水量', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='table1',
            name='使用部门',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='使用部门'),
        ),
    ]
