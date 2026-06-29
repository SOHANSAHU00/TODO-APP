from todo import views
from todo.views import *
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('toggle/<int:id>/', views.toggle, name='toggle'),
]
