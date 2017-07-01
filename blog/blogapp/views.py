from django.shortcuts import render
from  blogapp.models import Post


def post_list(request):
	post=Post.objects.all()
	return render(request,'post_list.html',{'post':post})