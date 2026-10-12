from django.shortcuts import render,redirect
from .models import Movie,Genre,Feedback


def get_movies(request):
    if request.method == "POST":
        movies = Movie.objects.all()
        return render(request,'movie.html',context={"cinema": movies})
    


def create_movies(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        photo = request.FILES.get("photo")
        Movie.objects.create(name = name,description = description,photo = photo)
        return redirect("movie.html")
    return render(request,"movie_create.html")


def update_movies(request,pk):
    movies = Movie.get(id=pk)
    if request.method == "POST":
        movies.name = request.POST.get("name")
        movies.description = request.POST.get("description")
        if request.FILES.get("photo"):
            movies.photo = request.FILES.get("photo")
        movies.save()
        return redirect("movies_detail",pk=movies.id)
    return render(request,"movie_update.html")


def delete_movies(request,pk):
    movies = Movie.get(id=pk)
    if request.method == "POST":
        movies.delete()
        return redirect("movie.html")
    return render(request,"delete_movies.html",context = {"movie":movies})


def create_genre(request):
    if request.method == "POST":
        name = request.POST.get("name")
        Genre.objects.create(name = name)
        return redirect()
    return render(request,"genre_create.html")


def create_feedback(request):
    if request.method == "POST":
        text = request.POST.get("name")
        Feedback.objects.create(text = text)
        return redirect(request,"movie.html")
