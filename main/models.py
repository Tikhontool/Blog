from django.db import models

from django.db import models
from django.contrib.auth.models import User




class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', blank=True, null= True)
    title = models.CharField('Заголовок', max_length=255)
    slug = models.SlugField('URL')
    intro = models.TextField('Краткое описание')
    body = models.TextField('Статья')
    date_added = models.DateTimeField(auto_now_add=True)
    img = models.ImageField('Картинка', upload_to='images/', blank=True )

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
            return self.title



class Comment(models.Model):
    post = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField()
    body = models.TextField(verbose_name='Текст')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']


