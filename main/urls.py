from . import views
from django.conf import settings  # new
from django.urls import path, include  # new
from django.conf.urls.static import static  # new


urlpatterns = [
    # path('', include('registration.urls')),
    path('', views.home, name='home'),
    path('', include('registration.urls')),
    path('blogs/', views.frontpage, name='blogs'),
    path('blogs/editing', views.editing, name='editing'),
    path('bloggers/', views.home, name='bloggers'),

    path('<slug:slug>/', views.post_detail, name='post_detail'),
    # path('', include('django.contrib.auth.urls')),




    #path('/blog/<blog-id>/create', views.home, name='blog_create'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    # path('registr/', views.registr, name='registr')
    # path('blogger/<author-id>', views.home, name='blogger_id'),
    # path('blog/<blog-id>', views.home, name='blog_id'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)