from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('Aboutme/', views.Aboutme, name="Aboutme"),
    path('create/', views.create, name="create"),
    path('<int:blog_id>/delete', views.delete, name="delete"),
    path('<int:blog_id>/edit' , views.edit, name="edit"),
    path('<int:blog_id>/update' , views.update , name="update"),
    




]
