# Generated by Django 3.2.18 on 2023-05-24 06:35

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
                ('title', models.CharField(default='', max_length=20, verbose_name='主任')),
                ('date', models.DateTimeField(verbose_name='更改日期')),
            ],
        ),
        migrations.CreateModel(
            name='table2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=20, verbose_name='副主任')),
                ('date', models.DateTimeField(verbose_name='更改日期')),
                ('bind', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.table1')),
            ],
        ),
        migrations.CreateModel(
            name='table3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=20, verbose_name='科员')),
                ('old', models.CharField(default='', max_length=20, verbose_name='年限')),
                ('date', models.DateTimeField(verbose_name='更改日期')),
                ('bind', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.table2')),
            ],
        ),
    ]
