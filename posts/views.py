from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Post
from django.shortcuts import get_object_or_404 
from .forms import PostForms
from django.contrib import messages
def home(request):
	return HttpResponse("<h1> Hello world </h1>")

def post_create(request):
	
	form = PostForms(request.POST or None)
	if form.is_valid():
		form.save()
		messages.success(request, "OMG! So Cool!")
		return redirect("posts:list")
	context = {
		"form":form,
	}
	return render(request, 'post_create.html', context)

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

def post_update(request, post_id):
	post_object = get_object_or_404(Post, id=post_id)
	form = PostForms(request.POST or None, instance=post_object)
	if form.is_valid():
		form.save()
		messages.success(request, "giving it a second thought?")
		return redirect("posts:list")
	context = {
		"form":form,
		"post_object":post_object,
	}
	return render(request, 'post_update.html', context)

def post_delete(request, post_id):
	Post.objects.get(id=post_id).delete()
	messages.warning(request, "You Sure?")
	return redirect("posts:list")


