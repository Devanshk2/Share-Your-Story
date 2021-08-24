from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('addblog',views.addblog,name='addblog'),
    path('',views.bloghome,name='bloghome'),
    path('<str:slug>',views.blogpost,name='blogpost'),
]