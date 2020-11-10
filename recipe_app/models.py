from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_requirment = models.CharField(max_length=50)
    instructions = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.author.name}'
