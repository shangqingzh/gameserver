# Generated by Django 2.2.8 on 2020-06-23 07:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientid', models.IntegerField(verbose_name='客户端号')),
                ('score', models.IntegerField(verbose_name='分数')),
                ('clientname', models.CharField(blank=True, max_length=32, null=True, verbose_name='昵称')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerScoreRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientid', models.CharField(max_length=32, verbose_name='客户端号')),
                ('score', models.IntegerField(verbose_name='分数')),
                ('operate_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='提交时间')),
            ],
        ),
    ]