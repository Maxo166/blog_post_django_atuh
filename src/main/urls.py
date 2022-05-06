from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('create_post', views.create_post, name='create_post'),
    path('post_detail/<int:id>', views.post_details, name='post_details'),
    path('edit_post/<int:id>', views.update_post, name='update_post'),
    path('password_change/', views.change_password, name='change_password'),
    path('user/create_userprofile/',
         views.create_userprofile, name='create_userprofile'),
    path('user/view_profile/<int:id>',
         views.view_userprofile, name='view_userprofile'),

]
