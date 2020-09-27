from django.contrib import admin
from django.urls import path,include
from . import views 



urlpatterns = [
   path('', views.showBlogs, name='blogs'),
   # API to Post a comment
   path('postcomment',views.postComment, name='postcomment'),
   path('<str:slug>', views.blogpost, name='blogpost'),

]