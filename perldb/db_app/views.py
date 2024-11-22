from django.shortcuts import get_object_or_404, render
from .models import BlogPost

# Create your views here.


def blog_list(request):
    posts = BlogPost.objects.all() #list from database
    return render(request, 'blog_list.html', {'posts': posts} )


def blog_detail(request, id):
    post = get_object_or_404(BlogPost, id=id) #show all details from db
    return render(request, 'blog_detail.html', {'post':post})