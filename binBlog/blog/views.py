from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.
def index(request):
    blog_list = Blog.objects.all()
    return render(request, 'index.html')

def blogs(request):
    blog_list = Blog.objects.all()
    # print(blog_list)
    return render(request, 'blogs.html', {'blog_list': blog_list})
def detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'detail.html', context={'blog': blog})