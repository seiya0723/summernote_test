from django.db import models

class Topic(models.Model):
    comment         = models.TextField(verbose_name="コメント")
