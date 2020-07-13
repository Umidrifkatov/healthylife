from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
from django.db.models import Q

def post_list(request):
    search_query = request.GET.get('search', '')
    
    if search_query:
        posts  = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()
    
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)


    return render(request, 'home.html', {'posts': page})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'post_detail.html', {'post': post})


def about(request):
    return render(request, 'about.html')