from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to = 'main/images')
    movie_genre = models.ForeignKey(Genre,on_delete=models.CASCADE,related_name="movies")

    def __str__(self):
        return self.name


class Feedback(models.Model):
    text = models.TextField()


    def __str__(self):
        return self.text