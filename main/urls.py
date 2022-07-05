from . import views
from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static  # new


urlpatterns = [
    # path('', include('registration.urls')),
    path('', views.home, name='home'),
    path('', include('registration.urls')),
    path('blogs/', views.Frontpage.as_view(), name='blogs'),
    path('blogs/editing', views.ArticleCreateView.as_view(), name='editing'),
    path('bloggers/', views.home, name='bloggers'),


    path('<slug:slug>/', views.post_detail, name='post_detail'),

    # path('update-page/<slug:slug>/', views.update_page, name='update_page'),
    # path('delete-page/<slug:slug>/', views.delete_page, name='delete_page'),




    #path('/blog/<blog-id>/create', views.home, name='blog_create'),

    # path('blogger/<author-id>', views.home, name='blogger_id'),
    # path('blog/<blog-id>', views.home, name='blog_id'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)