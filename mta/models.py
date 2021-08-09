from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=32, default='')
    event_en = models.CharField(max_length=32, default='')
    attribute_en = models.CharField(max_length=32, default='')
    event_sh = models.CharField(max_length=32, default='')
    type = models.CharField(max_length=32, default='')
    # 文章正文，使用的是TextField
    # 存储比较短的字符串可以使用 CharField，但对于文章的正文来说可能会是一大段文本，因此使用 TextField 来存储大段文本。
    description = models.TextField(null=True, default='')
    data = models.DateTimeField(auto_now = True)