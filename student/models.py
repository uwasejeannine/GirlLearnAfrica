from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    level_of_studies = models.CharField(max_length=100)
    program_interested_in = models.CharField(max_length=100)
    courses = models.ManyToManyField('Course', related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Mentor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    program_interested_in = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.username}"


class Course(models.Model):
    image = models.ImageField(upload_to='course_images/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)  

    def __str__(self):
        return self.name

class CommunityEvent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title
