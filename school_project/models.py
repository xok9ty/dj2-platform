from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    bio = models.TextField()
    num_classs = models.IntegerField()

    def __str__(self):
        return self.title

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    birthday = models.DateField()

    def __str__(self):
        return self.title
    
class Class(models.Model):
    num_class = models.IntegerField()
    floor = models.IntegerField()

    def __str__(self):
        return self.title

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    birthday = models.DateField()
    home_adress = models.CharField(max_length=200)
    head_teacher = models.CharField(max_length=100)
    class_num = models.IntegerField()

    def __str__(self):
        return self.title