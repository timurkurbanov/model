from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=255)

class Viewer(models.Model):
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    film = models.ManyToManyField(Film, related_name='viewers')



class Worker(models.Model):
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=255)

class Shift(models.Model):
    day = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    worker = models.ManyToManyField(Worker, related_name='shifts')




class Book(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=255)

class Chapter(models.Model):
    title = models.CharField(max_length=255)
    number = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='chapters')

class Reader(models.Model):
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    books_read = models.ManyToManyField(Book, related_name='readers')

class Author(models.Model):
    name = models.CharField(max_length=255)
    books_written = models.ManyToManyField(Book, related_name='authors')