from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import Post

import calendar


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def year_archive(request, year):
    posts = Post.objects.filter(pub_date__year=year)
    context = {'year': year, 'posts': posts}
    return render(request, 'blog/year_archive.html', context)


def month_archive(request, year, month):
    posts = Post.objects.filter(pub_date__year=year, pub_date__month=month)
    context = {'year': year, 'month': calendar.month_name[month], 'posts': posts}
    return render(request, 'blog/month_archive.html', context)


def post_detail(request, year, month, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if not (post.pub_date.year == year and post.pub_date.month == month):
        raise Http404('Post does not exist')
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)
