from django.db import models

from django_summernote.fields import SummernoteTextFormField, SummernoteTextField

class Topic(models.Model):

    # bleach にはstyles属性はないと言われ、エラーになるため、除去してTextFieldを使用
    #comment        = SummernoteTextField(verbose_name="コメント")

    comment         = models.TextField(verbose_name="コメント")
