# Generated by Django 3.2.18 on 2023-06-08 08:00

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
                ('年份', models.CharField(blank=True, default='', max_length=20, verbose_name='年份')),
                ('月份', models.CharField(blank=True, default='', max_length=20, verbose_name='月份')),
            ],
        ),
    ]
