from django import forms 
from .models import Topic

from django_summernote.fields import SummernoteTextFormField, SummernoteTextField

# XXX:requestsやcurlから直接リクエストを送信し、scriptタグやonclick属性を使用してJavaScriptを書かれるとXSSが成立する。
# https://teratail.com/questions/254484
# https://github.com/summernote/django-summernote/issues/391

import bleach
from django import forms
from django_summernote.widgets import SummernoteWidget

ALLOWED_TAGS = [
    'a', 'div', 'p', 'span', 'img', 'em', 'i', 'li', 'ol', 'ul', 'strong', 'br',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'table', 'tbody', 'thead', 'tr', 'td',
    'abbr', 'acronym', 'b', 'blockquote', 'code', 'strike', 'u', 'sup', 'sub',
]
"""
STYLES = [
    'background-color', 'font-size', 'line-height', 'color', 'font-family'
]
"""
ATTRIBUTES = {
    '*': ['style', 'align', 'title', ],
    'a': ['href', ],
}


class HTMLField(forms.CharField):

    def __init__(self, *args, **kwargs):
        super(HTMLField, self).__init__(*args, **kwargs)
        self.widget = SummernoteWidget()

    # ここで.clean()内にstyles引数を入れるとエラー
    def to_python(self, value):
        value       = super(HTMLField, self).to_python(value)
        return bleach.clean(value, tags=ALLOWED_TAGS, attributes=ATTRIBUTES)


class TopicForm(forms.ModelForm):
    class Meta:
        model   = Topic
        fields  = [ "comment" ]
        #widgets = { "comment": SummernoteWidget() }

    #comment = SummernoteTextField() # ←これは発動しなかった？これを有効化し、attacker.pyを動かすとXSSが通る
    comment = HTMLField()

