from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass



# class Actor(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     date_of_birth = models.DateField()
#     age = models.IntegerField()

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"


# class Actress(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     date_of_birth = models.DateField()
#     age = models.IntegerField()


#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"


class Cast(models.Model):
    Actor = 'A+'
    Actress = 'A'
    CAST = (
        (Actor , 'Actor'),
        (Actress , 'Actress')
    )
    category = models.CharField(choices=CAST , default=Actor, max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    age = models.IntegerField()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    

class Director(models.Model):
    first_name = models.CharField(max_length=50)    
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.first} {self.last_name}"
    

class Movie(models.Model):
    cast = models.ManyToManyField(Cast)
    title = models.CharField(max_length=50)
    Directed_by = models.ManyToManyField(Director)
    genre = models.CharField(max_length=50)
    runtime = models.CharField(max_length=50)
    year = models.IntegerField()


    def __str__(self):
        return self.title



