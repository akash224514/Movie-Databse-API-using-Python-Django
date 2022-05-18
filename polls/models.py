from django.db import models

from django.forms import ModelForm

# Create your models here.

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.CharField(null=True,max_length=200)
    genre=models.CharField(null=True, max_length=50)
    writer = models.CharField(null=True, max_length=50)
    plot = models.CharField(null=True, max_length=50)
    director = models.CharField(null=True, max_length=50)
    awards = models.CharField(null=True, max_length=50)
    Type = models.CharField(null=True, max_length=50)
    Actors = models.CharField(null=True, max_length=50)
    imdbRating = models.FloatField(null=True)
    Poster = models.ImageField

class Subject(models.Model):
   subject_id = models.PositiveIntegerField(primary_key=True, db_column='subject_id')
   name = models.CharField(max_length=255)
   max_marks = models.PositiveIntegerField()


class  MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title']
