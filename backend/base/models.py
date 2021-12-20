from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    user=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    genre=models.CharField(max_length=200,null=True,blank=True)
    rating_id=models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    release_date=models.CharField(max_length=200,null=True,blank=True)
    actors=models.CharField(max_length=200,null=True,blank=True)
    bio=models.CharField(max_length=200,null=True,blank=True)
    review_id=models.IntegerField(default=0,null=True,blank=True)
    front_pic =models.ImageField(null=True,blank=True,default='/placeholder.png')
    
    _id=models.AutoField(primary_key=True,editable=False)


    def __str__(self):
        return self.name

class Review(models.Model):
    movie_id = models.IntegerField(default=0,null=True,blank=True)
    user_id = models.IntegerField(default=0,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    comment=models.TextField(null=True,blank=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return str(self._id)

class Rating(models.Model):
    movie_id = models.IntegerField(default=0,null=True,blank=True)
    user_id = models.IntegerField(default=0,null=True,blank=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    rating = models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return str(self._id)
class Moderating(models.Model):
    user_id = models.IntegerField(default=0,null=True,blank=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    score = models.IntegerField(default=0,null=True,blank=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return str(self.score)

class List(models.Model):
    user_id = models.IntegerField(default=0,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    movies = models.CharField(max_length=200,null=True,blank=True)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return str(self.movies)