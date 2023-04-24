from django.shortcuts import render,redirect

from django.views import View


from .models import Topic
from .forms import TopicForm

class IndexView(View):

    def get(self, request, *args, **kwargs):

        context = {}
        context["topics"]  = Topic.objects.all()
        context["form"]    = TopicForm()

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):
        
        form    = TopicForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect("bbs:index")

index   = IndexView.as_view()
