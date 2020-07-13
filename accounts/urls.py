from django.urls import path , re_path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('register/', views.register , name='register'),
    path('test/<slug>', views.test),
    path('login/', views.login_view , name='login'),
    path('logout/', views.logout_view , name='logout'),
    path('profile/<slug>/', views.profile , name='profile'),
    path('profile/<slug>/edit', views.edit_profile , name='edit_profile'),
    path('change-password/<slug>/', views.passwordchange_view , name='change_password'),
]

