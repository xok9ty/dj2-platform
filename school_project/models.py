from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    birthday = models.DateField()

    def __str__(self):
        return self.first_name
    

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    bio = models.TextField()
    num_classs = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.subject_name


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
        return self.first_name
    

class Class(models.Model):
    num_class = models.IntegerField()
    floor = models.IntegerField()
    student = models.ManyToManyField(Student)

    def __str__(self):
        return self.num_class