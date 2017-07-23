from django.shortcuts import render
from django.http import HttpResponse
from.models import Post
from django.shortcuts import get_object_404 
def home(request):
	return HttpResponse("<h1> Hello world </h1>")
def post_create(request):
	obj = get_object_or_or_404(post, id=100000)
	context = {
	"title"
	}
	return render(request, 'create.html', context)

def post_detail(request): 
	objects_list=Post.objects.all()
	objects_get=Post.objects.get(id=1)
	context = {
		"objects_list": objects_list,
		"title": "List",
		"user": request.user,
		"objects_get": objects_get,
	}
	return render(request, 'create2.html', context)

def post_list(request):
	return render(request, 'create3.html', {})

def post_update(request):
	return render(request, 'create4.html', {})

def post_delete(request):
	return render(request, 'create5.html', {})
