from django import forms 

from django_summernote.widgets import SummernoteWidget
from django.conf import settings

from .models import Topic

import bleach


# style属性を許可する場合、 CSSSanitizerをbleach.clean()の引数に入れる
# 前もって、 pip install tinycss2 を実行しておく
from bleach.css_sanitizer import CSSSanitizer
#css = CSSSanitizer(allowed_css_properties=[]) # 個別に許可をしたい場合はここに文字列型で許可するCSSのプロパティを入れる
css = CSSSanitizer() # すべてのCSSを許可する場合はこうする。



class HTMLField(forms.CharField):

    def __init__(self, *args, **kwargs):
        super(HTMLField, self).__init__(*args, **kwargs)
        self.widget = SummernoteWidget()

    # ここで.clean()内にstyles引数を入れるとエラー(bleachはstyle引数は廃止されている)
    def to_python(self, value):
        value       = super(HTMLField, self).to_python(value)
        return bleach.clean(value, tags=settings.ALLOWED_TAGS, attributes=settings.ATTRIBUTES, css_sanitizer=css )


class TopicForm(forms.ModelForm):
    class Meta:
        model   = Topic
        fields  = [ "comment" ]

    comment = HTMLField()

