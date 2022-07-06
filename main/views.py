from django.core.checks import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import CommentForm,ArticleForm
from .models import News
from django.views.generic import ListView, DetailView,CreateView, UpdateView,DeleteView


class Home(ListView):
    model = News
    template_name = 'main/main_page.html'
    context_object_name = 'posts'


class Frontpage(ListView):
    model = News
    template_name = 'main/frontpage.html'
    context_object_name = 'posts'



# class Authors(ListView):
#     model = News
#     template_name = 'main/authors_page.html'
#     context_object_name = 'posts'


def authors(request):

    return (request, 'main/authors_page.html')


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



# class Post_detail ( CreateView):
#     model = News
#     template_name = 'main/post_detail.html'
#     form_class = CommentForm
#     success_url = reverse_lazy('post_detail')
#
#     def get_context_data(self, **kwargs):
#         kwargs['post'] = News.objects.all().order_by('-id')
#         return super().get_context_data(**kwargs)
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.post = self.request.user
#         self.object.save()
#         return super().form_valid(form)



class ArticleCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = News
    template_name = 'main/editing.html'
    form_class = ArticleForm
    success_url = reverse_lazy('editing')
    success_msg = 'Запись создана'

    def get_context_data(self, **kwargs):
        kwargs['posts'] = News.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = News
    template_name = 'main/editing.html'
    form_class = ArticleForm
    success_url = reverse_lazy('editing')
    success_msg = 'Запись успешно обновлена'
    def get_context_data(self,**kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs




class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = News
    template_name = 'main/editing.html'
    success_url = reverse_lazy('editing')

    def post(self,request,*args,**kwargs):
        return super().post(request)

    def form_valid(self, form, **kwargs):
        self.object = self.get_object()
        if self.request.user == self.object.author:
            success_url = self.get_success_url()
            self.object.delete()
            return HttpResponseRedirect(success_url)
        else:
            return self.handle_no_permission()





















































