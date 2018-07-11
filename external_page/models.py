from django.db import models

# Create your models here.

class Hobby(models.Model):
    hobby_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.hobby_name

class Instructor(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    hobbies = models.ManyToManyField(Hobby)
    email = models.EmailField(max_length=256, blank=True, null=True, unique=True)
    city = models.CharField(max_length=128, null=False)
    zip_code = models.CharField(max_length=10, null=False)
    description = models.TextField(max_length=2048, null=True, default=None)
    gender = models.CharField(max_length=1,
                           choices=(
                                    ('M', 'Male'),
                                    ('F', 'Female')
                           )
                           )
    work_in_student_home = models.BooleanField(default=False)
    work_in_instructor_home = models.BooleanField(default=True)
    maximum_students = models.PositiveIntegerField(default=2)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Grade(models.Model):
    pass
    # Connect (instructor-hobby) to user grade of that (instructor-hobby) combination