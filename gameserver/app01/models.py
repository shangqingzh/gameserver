from django.db import models
from django.utils import timezone

# Create your models here.


# 用户分数表
class PlayerScore(models.Model):
    clientid = models.IntegerField(verbose_name="客户端号")
    score = models.IntegerField(verbose_name="分数")
    clientname = models.CharField(max_length=32, verbose_name="昵称", null=True, blank=True)


# 用户分数提交记录
class PlayerScoreRecord(models.Model):
    clientid = models.CharField(max_length=32, verbose_name="客户端号")
    score = models.IntegerField(verbose_name="分数")
    operate_time = models.DateTimeField(default=timezone.now, verbose_name="提交时间")
