from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('create_post', views.create_post, name='create_post'),
    path('posts/<int:id>', views.post_details, name='post_details'),
    path('password_change/', views.change_password, name='change_password'),

]
