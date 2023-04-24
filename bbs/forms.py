from django import forms 

from django_summernote.widgets import SummernoteWidget
from django.conf import settings

from .models import Topic

import bleach



class HTMLField(forms.CharField):

    def __init__(self, *args, **kwargs):
        super(HTMLField, self).__init__(*args, **kwargs)
        self.widget = SummernoteWidget()

    # ここで.clean()内にstyles引数を入れるとエラー(bleachはstyle引数は廃止されている)
    def to_python(self, value):
        value       = super(HTMLField, self).to_python(value)
        return bleach.clean(value, tags=settings.ALLOWED_TAGS, attributes=settings.ATTRIBUTES)


class TopicForm(forms.ModelForm):
    class Meta:
        model   = Topic
        fields  = [ "comment" ]

    comment = HTMLField()

