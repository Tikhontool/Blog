from . import views
from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static  # new


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('', include('registration.urls')),
    path('blogs/', views.Frontpage.as_view(), name='blogs'),
    path('blogs/editing/', views.ArticleCreateView.as_view(), name='editing'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('bloggers/', views.authors, name='bloggers'),

    path('update-page/<int:pk>/', views.ArticleUpdateView.as_view(), name='update_page'),
    path('delete-page/<int:pk>/', views.ArticleDeleteView.as_view(), name='delete_page'),







    #path('/blog/<blog-id>/create', views.home, name='blog_create'),
    # path('blogger/<author-id>', views.home, name='blogger_id'),
    # path('blog/<blog-id>', views.home, name='blog_id'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)