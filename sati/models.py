from django.db import models
from django.db.models import Model


class Person(Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    class Meta:
        abstract = True


class Mentor(Person):
    pass


class Student(Person):
    pass


class Course(Model):
    course_description = models.CharField(max_length=200)
    student = models.CharField(max_length=50)
    mentor = models.CharField(max_length=50)
    class_quantity = models.PositiveIntegerField()

    objects = models.Manager()


class Class(Model):
    class_description = models.CharField(max_length=200)
    class_price = models.FloatField()
    class_duration = models.PositiveIntegerField()
    date_time = models.DateTimeField()
    paid = models.BooleanField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)

    objects = models.Manager()
