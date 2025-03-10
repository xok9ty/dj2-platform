from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
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
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    birthday = models.DateField()
    home_address = models.CharField(max_length=200)
    class_num = models.IntegerField()

    def __str__(self):
        return self.first_name
    

class Class(models.Model):
    num_class = models.IntegerField()
    name_class = models.CharField(max_length=5)
    student = models.ManyToManyField(Student)
    head_teacher = models.CharField(max_length=100)

    def __str__(self):
        return self.num_class