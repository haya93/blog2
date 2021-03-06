from __future__ import unicode_literals
from django.contrib import admin
from .models import *

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "timestamp", "updated"]
	class Meta:
		model = Post

admin.site.register (Post, PostModelAdmin)
admin.site.register(Like)
