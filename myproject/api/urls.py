from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_user, name = 'get_user'), 
    path('create/', views.post_user, name = 'post_user'),
    path('<int:pk>/update/', views.update_user, name = 'update_user'),
    path('<int:pk>/delete/', views.delete_user, name = 'delete_user'),

]