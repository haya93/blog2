from django.shortcuts import render
from django.http import HttpResponse
from.models import Post
from django.shortcuts import get_object_or_404 
def home(request):
	return HttpResponse("<h1> Hello world </h1>")
def post_create(request):
	
	context = {
	"title"
	}
	return render(request, 'create.html', context)

def post_detail(request, post_id): 
	obj = get_object_or_404(Post, id=post_id)
	
	context = {
		"instance": obj,
	}
	return render(request, 'post_detail.html', context)

def post_list(request):
	
	objects_list=Post.objects.all()
	context = {
	"post_list": objects_list,
	}
	return render(request, 'post_list.html', context)

def post_update(request):
	return render(request, 'create4.html', {})

def post_delete(request):
	return render(request, 'create5.html', {})
