# Generated by Django 3.2.14 on 2023-03-10 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='table1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=20, verbose_name='公司名')),
            ],
        ),
        migrations.CreateModel(
            name='table2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=20, verbose_name='气体')),
                ('bind', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='武汉分公司气耗.table1')),
            ],
        ),
        migrations.CreateModel(
            name='table3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=20, verbose_name='比较')),
                ('bind', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='武汉分公司气耗.table2')),
            ],
        ),
        migrations.CreateModel(
            name='table4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.FloatField(default=0.0, verbose_name='消耗(吨)')),
                ('date', models.DateTimeField(verbose_name='选择月份')),
                ('bind', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='武汉分公司气耗.table3')),
            ],
        ),
    ]
