from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    bio = models.TextField()
    num_classs = models.CharField(max_length=10)

    def __str__(self):
        return self.title

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    birthday = models.DateField()

    def __str__(self):
        return self.title
    
class Class(models.Model):
    num_class = models.CharField(max_length=10)
    floor = models.CharField(max_length=2)

    def __str__(self):
        return self.title

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    birthday = models.DateField()
    class_num = models.CharField(max_length=10)

    def __str__(self):
        return self.title