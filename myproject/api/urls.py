from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_user, name = 'get_user'), 
    path('post/', views.post_user, name = 'post_user'),
]