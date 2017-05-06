# coding: utf-8
from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(u'任务名', max_length=255)
    content = models.TextField(u'任务内容', blank=True, null=True)
    is_finished = models.BooleanField(u'完成', default=False)
    expired_date = models.DateField(u'过期时间', blank=True, null=True)
    created_at = models.DateTimeField(u'创建时间', auto_now_add=True)
