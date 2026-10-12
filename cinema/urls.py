from django.urls import path
from .views import *

urlpatterns = [
    path("",get_movies,name = "get_movies"),
    path("create/", create_movies, name="create_movies"),
    path("<int:pk>/update/", update_movies, name="update_movies"),
    path("<int:pk>/delete/", delete_movies, name="delete_movies"),
    path("",create_genre,name = "create_genre")
]