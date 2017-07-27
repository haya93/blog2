from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Post
from django.shortcuts import get_object_or_404 
from .forms import PostForms
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import quote



def home(request):
	return HttpResponse("<h1> Hello world </h1>")

def post_create(request):
	
	form = PostForms(request.POST or None, request.FILES or None, )
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
		"share_string": quote(obj.content)
	}
	return render(request, 'post_detail.html', context)

def post_list(request):
	
	obj_list = Post.objects.all()
	paginator = Paginator(obj_list, 4) 

	page = request.GET.get('page')
	try:
		objs = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		objs = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		objs = paginator.page(paginator.num_pages)

	
	context = {
	"post_list": objs,
	}
	return render(request, 'post_list.html', context)

def post_update(request, post_id):
	post_object = get_object_or_404(Post, id=post_id)
	form = PostForms(request.POST or None, request.FILES or None, instance=post_object)
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


