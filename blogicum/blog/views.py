from datetime import datetime

from django.shortcuts import get_object_or_404, get_list_or_404, render

from blog.models import Post


def index(request):
    """Возвращает главную страницу."""
    template_name = 'blog/index.html'
    post_list = Post.objects.select_related(
        'category'
    ).filter(
        is_published=True,
        pub_date__lte=datetime.now(),
        category__is_published=True
    ).order_by('-pub_date')[0:5]
    context = {'post_list': post_list}
    return render(request, template_name, context)


def post_detail(request, pk):
    """Возвращает заданный пост."""
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        is_published=True,
        pub_date__lte=datetime.now(),
        category__is_published=True,
        pk=pk
    )
    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    """Возвращает посты в заданной категории."""
    template_name = 'blog/category.html'
    post_list = get_list_or_404(
        Post,
        category__slug=category_slug,
        is_published=True,
        pub_date__lte=datetime.now(),
        category__is_published=True
    )
    context = {'post_list': post_list}
    return render(request, template_name, context)
