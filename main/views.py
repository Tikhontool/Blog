from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import CommentForm,ArticleForm
from .models import News
from django.views.generic import ListView, DetailView,CreateView, UpdateView,DeleteView


def home(requests):

    return render(requests, 'main/main_page.html')



class Frontpage(ListView):
    model = News
    template_name = 'main/frontpage.html'
    context_object_name = 'posts'



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



def edit_page(request):
    success = False
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            success = True

    template = 'edit_page.html'
    context = {
        'list_articles': News.objects.all().order_by('-id'),
        'form': ArticleForm(),
        'success': success
    }
    return render(request, template, context)



def editing(request):
    success = False
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            News.author = request.user
            form.save()
            # img_obj = form.instance

            success = True

    template = 'main/editing.html'
    context = {
        'posts': News.objects.all(),
        'form': ArticleForm(),
        'success': success
    }

    return render(request, template, context)




class ArticleCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')                       #ссылка на страницу, которая будет выходить, для незарегестрированных пользователей
    model = News
    template_name = 'main/editing.html'
    form_class = ArticleForm
    success_url = reverse_lazy('editing')                   #ссылка на страницу, после удачного входа
    success_msg = 'Запись создана'

    def get_context_data(self, **kwargs):
        kwargs['posts'] = News.objects.all().order_by('-id')  # Не понятно
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


def update_page(request, pk):
    success_update = False
    get_article = News.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=get_article)
        if form.is_valid():
            form.save()
            success_update = True
    template = 'edit_page.html'
    context = {
        'get_article': get_article,
        'update': True,
        'form': ArticleForm(instance=get_article),
        'success_update': success_update

    }
    return render(request, template, context)


def delete_page(request, pk):
    get_article = News.objects.get(pk=pk)
    get_article.delete()

    return redirect(reverse('edit_page'))


















































