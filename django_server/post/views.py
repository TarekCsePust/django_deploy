from django.shortcuts import render,redirect
from .forms import CreateForm
from .models import Post
# Create your views here.

def CreatePost(request):
	form = CreateForm(request.POST or None,request.FILES or None)
	if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                return redirect('/post')
	return render(request, "create.html", {"form": form})

def Index(request):
	posts = Post.objects.all()
	return render(request, "index.html", {"posts": posts})

