from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('',tweetlist,name="tweetlist" ),
    path('create/',tweetcreate,name="create" ),
    path('<int:tweetid>/edit/',tweetedit,name="edit" ),
    path('<int:tweetid>/delete/',tweetdelete,name="delete" ),
    path('register/',register,name="register" ),
]