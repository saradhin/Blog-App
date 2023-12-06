from django.shortcuts import render
from blog.models import Post, Comment, Category

# Create your views here.
def blog_index(request):
    """blog index to list blog posts"""
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts" : posts
    }
    return render(request, "blog/index.html", context)

def blog_category(request, category):
    """list blog categories"""

    posts = Post.objects.filter(categories__name__contains=category).order_by("-created_on")
    context = {
        "category" : category,
        "posts": posts
    }
    return render(request, "blog/category.html", context)

def blog_detail(request, pk):
    """View for blog details"""

    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments
    }

    return render(request, "blog/detail.html", context)