from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

class Order(models.Model):
    number = models.CharField(max_length=255)
    date = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')



class Author(models.Model):
    name = models.CharField(max_length=255)

class Book (models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')



class City(models.Model):
    city_name = models.CharField(max_length=255)
    year_founded = models.CharField(max_length=255)

class Residence(models.Model):
    address = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='residences') 

class Person(models.Model):
    name = models.CharField(max_length=255)
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE, related_name='habitants') 
