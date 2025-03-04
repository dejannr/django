from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my_app/', views.post_list, name='post_list'),
    path('my_app/<int:pk>/', views.post_detail, name='post_detail'),
    path('my_app/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('my_app/create/', views.post_create, name='post_create'),
]