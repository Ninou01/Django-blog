from django.urls import path 
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home , name='home'),
    path('posts-of-<slug>', views.user_posts , name='user_posts'),
    path('post/<slug>', views.post , name='post'),
    path('create/', views.create_post , name='create'),
    path('post/<slug>/edit', views.edit , name='edit'),
    path('post/<slug>/delete', views.delete , name='delete'),
        
]
