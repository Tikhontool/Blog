
from .models import Comment
from django import forms
from .models import News

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class ArticleForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'slug', 'intro', 'body', 'img']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
