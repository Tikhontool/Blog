from django.shortcuts import render, redirect
from .forms import CommentForm,ArticleForm
from .models import News






def home(requests):

    return render(requests, 'main/main_page.html')


def frontpage(request):
    posts = News.objects.all()

    return render(request, 'main/frontpage.html', {'posts': posts})

def post_detail(request, slug):
    post = News.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'main/post_detail.html', {'post': post, 'form': form})

# def editing(request):
#     success = False
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             success = True
#     posts = News.objects.all()
#     # form = ArticleForm
#     return render(request, 'main/editing.html', {'posts': posts, 'form': form, 'success':success})


def editing(request):
    success = False
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            success = True

    template = 'main/editing.html'
    context = {
        'posts': News.objects.all(),
        'form': ArticleForm(),
        'success': success
    }
    return render(request, template, context)